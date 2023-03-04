from multiprocessing import Process, Pipe
import key_functions



class Detections:
    def __init__(self):
        self.conn_AP_find_faces, self.conn_BP_find_faces = Pipe()  # generate a pipe for communication between processes
        find_facesProcess = Process(target=key_functions.find_faces,
                                    args=(self.conn_BP_find_faces,))




        self.conn_AP_direct_output, self.conn_BP_direct_output = Pipe()  ## generate a pipe for communication between processes
        direct_outputProcess = Process(target=key_functions.directOutput,
                                       args=(self.conn_BP_direct_output,))


        #launch the processes
        find_facesProcess.start()

        direct_outputProcess.start()


