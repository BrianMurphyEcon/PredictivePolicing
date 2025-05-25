********************************************************************************
* MASTER DO-FILE FOR PREDICTIVE POLICING PROJECT
********************************************************************************

*** Define main directory
global main "C:\Users\bmmur\UH-ECON Dropbox\Brian Murphy\RA-TA\Predictive Policing Team"

*** Define subdirectories 
global code "$main\Code"
global data "$main\Data"
global temp "$data\temp"

* Yearly data folders
global y2016 "$data\2016"
global y2017 "$data\2017"
global y2018 "$data\2018"
global y2019 "$data\2019"
global y2020 "$data\2020"
global y2021 "$data\2021"
global y2022 "$data\2022"

* Police department data
global police "$data\PoliceDept"

*** Log file ***
*log using "$main\master_log.smcl", replace

*** Load or run scripts here ***
do "$code\10 Analysis.do"

*** Close log ***
*log close
