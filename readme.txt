1, Abstract
This is a benchmark dataset of surface electromyogram (sEMG) in non-ideal conditions (SeNic). The dataset mainly consists of 8-channel sEMG signals, and electrode shifts from an 3D-printed annular ruler. A total of $30$ subjects participate in our data acquisition experiments of 7 gestures in non-ideal conditions, where non-ideal factors of 1) electrode shifts, 2) individual difference, 3) muscle fatigue, 4) inter-day difference, and 5) arm postures are elaborately involved.


2，Description
See the corresponding paper for details:
Bo Zhu, et al.. A Benchmark Dataset for sEMG-Based Gesture Recognition in Non-ideal Conditions. IEEE Trans. NSRE. VOL. xx, NO. x MONTH YEAR. (under review)
When the paper review is completed, it will be placed in the sub-folder of the data set in time. The data set is an open source data set. The paper(after the paper is published) is expected to be cited if the data set is used for research. The code related to the paper will be open sourced with the paper after the final draft of the paper is confirmed.


3, How To Use
  1) Download all files or individual files
  2）Unzip to the current folder
  3）Read files and file names through your program
  
  File and folder structure：
      Root directory: SeNic/
      The file 'SubjectsInfo.xlsx' records the information of all subjects.
      Each compressed file ‘hxx’ or folder ‘hxx’ starting with ‘h’ in the root directory 'SeNic/' represents the data of a subject. The folder name 'hxx' presents the      anonymous name of this subject, and you can find the corresponding information in the file “SubjectsInfo.xlsx” accordingly.
      Under each ‘hxx’ folder, there are several ‘Angle_h0_xx.xlsx’ files and './xx/' second-level subfolders, and each 'Angle_h0_xx.xlsx' file and './xx/' folder correspond to their names. The variable 'xx'in the file/folder name represents the xxth collection of the subject (xxth session). Note that all numbers start from 0.
      
  
  

