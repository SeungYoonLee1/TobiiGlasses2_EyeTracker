import time
from tobiiglassesctrl.controller import TobiiGlassesController

if hasattr(__builtins__, 'raw_input'):
    input = raw_input


def main():
    f = open("C:/Users/SYOONI/Desktop/gaze_point.txt", "w")

    tobiiglasses = TobiiGlassesController()
    print(tobiiglasses.get_battery_info())
    print(tobiiglasses.get_storage_info())

    if tobiiglasses.is_recording():
        rec_id = tobiiglasses.get_current_recording_id()
        tobiiglasses.stop_recording(rec_id)

    project_name = input("Please insert the project's name: ")
    project_id = tobiiglasses.create_project(project_name)

    participant_name = input("Please insert the participant's name: ")
    participant_id = tobiiglasses.create_participant(project_id, participant_name)

    calibration_id = tobiiglasses.create_calibration(project_id, participant_id)
    input("Put the calibration marker in front of the user, then press enter to calibrate")
    tobiiglasses.start_calibration(calibration_id)

    res = tobiiglasses.wait_until_calibration_is_done(calibration_id)

    if res is False:
        print("Calibration failed!")
        exit(1)

    recording_id = tobiiglasses.create_recording(participant_id)
    print("Important! The recording will be stored in the SD folder projects/%s/recordings/%s" % (
    project_id, recording_id))
    input("Press enter to start recording")
    tobiiglasses.start_recording(recording_id)
    tobiiglasses.send_custom_event("start_recording", "Start of the recording ")



    tobiiglasses.start_streaming()
    while True:

        try:
            time.sleep(0.033)
            gp_data = str(tobiiglasses.get_data()["gp"])
            if "-1" in gp_data:
                pass
            else:
                index1 = gp_data.find("[")
                index2 = gp_data.find("]")
                gp_data = gp_data[index1 + 1:index2]
                gp_data = gp_data.replace(",", "")
                gp_data = gp_data.replace("\n", "")
            f.write(gp_data)
            f.write("\n")


        except(KeyboardInterrupt):
            break



    tobiiglasses.send_custom_event("stop_recording", "Stop of the recording " + str(recording_id))
    tobiiglasses.stop_recording(recording_id)


    if res is False:
        print("Recording failed!")
        exit(1)

if __name__ == '__main__':
    main()