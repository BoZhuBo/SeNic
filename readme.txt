1, Abstract
This is a benchmark dataset of surface electromyogram (sEMG) in non-ideal conditions (SeNic). The dataset mainly consists of 8-channel sEMG signals, and electrode shifts from an 3D-printed annular ruler. A total of 36 subjects participate in our data acquisition experiments of 7 gestures in non-ideal conditions, where non-ideal factors of 1) electrode shifts, 2) individual difference, 3) muscle fatigue, 4) inter-day difference, and 5) arm postures are elaborately involved.


2，Description
See the corresponding paper for details:

B. Zhu, D. Zhang, Y. Chu, Y. Gu and X. Zhao, "SeNic: An Open Source Dataset for sEMG-Based Gesture Recognition in Non-Ideal Conditions," in IEEE Transactions on Neural Systems and Rehabilitation Engineering, vol. 30, pp. 1252-1260, 2022, doi: 10.1109/TNSRE.2022.3173708.

This paper is expected to be cited if the data set is used for research. 


3, How To Use
  1) Download all files or individual files
  2）Unzip to the current folder
  3）Read files and file names through your program
  
  File and folder structure：
      Root directory: SeNic/
      The file 'SubjectsInfo.xlsx' records the information of all subjects.
      Each compressed file 'hxx' or folder 'hxx' starting with 'h' in the root directory 'SeNic/' represents the data of a subject. The folder name 'hxx' presents the  anonymous name of this subject, and you can find the corresponding information in the file “SubjectsInfo.xlsx” accordingly.
      Under each ‘hxx’ folder, there are several ‘Angle_h0_xx.xlsx’ files and './xx/' second-level subfolders, and each 'Angle_h0_xx.xlsx' file and './xx/' folder correspond to their names. The variable 'xx'in the file/folder name represents the xxth collection of the subject (xxth session). Note that all numbers start from 0.
      (Error correction: the gender of h35 should be female, it is marked as male in the paper.)
      (The baseline code is being sorted out, and will be open sourced after the sorting is completed.)
  
  

