import excel using "C:\Users\bmmur\UH-ECON Dropbox\Brian Murphy\RA-TA\Predictive Policing Team\Data\2017\united_states_offense_type_by_agency_2017.xls", firstrow clear

gen obs_order = _n
sort obs_order

gen state_filled = State
replace state_filled = state_filled[_n-1] if missing(state_filled)

gen agency_filled = AgencyType
replace agency_filled = agency_filled[_n-1] if missing(agency_filled)

drop State AgencyType
rename state_filled State
rename agency_filled AgencyType

drop if Population1 <= 10000
drop if Population1 == .
duplicates list State AgencyType AgencyName

save "$temp\NIBRS2017_collapse.dta", replace

use "$police\cleaned_data", clear
drop in 258
rename agency_name AgencyName
rename state State
rename agency_type AgencyType
duplicates list State AgencyType AgencyName
drop if State =="nan"

merge 1:1 State AgencyType AgencyName using "$temp\NIBRS2017_collapse"

gen crime_percap = TotalOffenses / Population1

gen violent_crimes = AssaultOffenses + HomicideOffenses
gen violent_crimes_percap = violent_crimes / Population1

tab use_pred_pol

gen Predictive = 0

replace Predictive = 1 if inlist(use_pred_pol, ///
    "Yes", "Yes*", "Yes (See note)", ///
    "Hybrid", "Hybrid (see note)", ///
    "No? hybrid?")
	
gen num_contact = ///
    (datecontact1 != "") + ///
    (datecontact2 != "") + ///
    (datecontact3 != "") + ///
    (datecontact4 != "") + ///
    (datecontact5 != "")

gen log_pop = log(Population1)

reghdfe violent_crimes log_pop num_contact Predictive, absorb(State AgencyType) vce(cluster State)
