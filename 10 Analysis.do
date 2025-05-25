use "$y2017\NIBRS2017", clear
append using "$y2018\NIBRS2018"
...
merge m:1 ___ using "$police\cleaned_data"
