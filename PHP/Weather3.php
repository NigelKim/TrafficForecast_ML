<!DOCTYPE html>

<html>
<head>
    <title>Weather data</title>
</head>

<body>
<?php

require 'database.php';
//$dataPOST = trim(file_get_contents('php://input'));
//$data = json_decode(file_get_contents('/Users/Nigel/Desktop/Wash U/2018 Junior Spring/Research-ML/code/chicagoweatherhistory.json'));
$dataraw = file_get_contents('http://ec2-18-218-68-246.us-east-2.compute.amazonaws.com/~nigelkim/researchSP18/chicagoweatherhistory.json');

$pos2016end3 = strrpos($dataraw, "2016-12") + 31;
$pos2017start1 = $pos2016end3+1;
$pos2017end1 = strrpos($dataraw, "2017-06-30") + 31;
$pos2017start2 = $pos2017end1+1;
$pos2017end2 = strrpos($dataraw, "2017-12-31") + 31;
$pos2018start = $pos2017end2+1;
$pos2018end = strrpos($dataraw, "2018-") + 31;

$data2017a = json_decode("[".substr($dataraw, $pos2017start1, $pos2017end1-$pos2017start1)."]");
$data2017b = json_decode("[".substr($dataraw, $pos2017start2, $pos2017end2-$pos2017start2)."]");
$data2018 = json_decode("[".substr($dataraw, $pos2018start, $pos2018end-$pos2018start)."]");
$yrArray = array();
;
array_push($yrArray, $data2017a);
array_push($yrArray, $data2017b);
array_push($yrArray, $data2018);

$checker = 2017;
//print_r($yrArray[2]);
foreach($yrArray as $yrData){
    echo " accessed ".$checker;
    foreach((array) $yrData as $hourly){
        //print_r($hourly);
    //for($i=0; $i<count($data); $i++){
        
        $temperature = (double) $hourly->main->temp;      // temperature in Kelvin
        $windspeed = (double) $hourly->wind->speed;       // wind speed in m/s
        
        $datetimeRaw = $hourly->dt_iso;     				// date and time in "20XX-XX-XX XX:00:00 +0000 UTC"
        if (substr($datetimeRaw,11,2) == "00"){         // comment this out if we want to get ALL POSSIBLE HOURLY DATA.
                                                        // currently, only getting 00:00 data
            $year = substr($datetimeRaw,0, 4);              // year
            //echo $datetimeRaw[5];
            //echo $year;
            if ($datetimeRaw[5] == 0){                      // month
                $month = $datetimeRaw[6];
            }
            else {
                $month = substr($datetimeRaw,5, 2);
                //echo $month;
            }
            if ($datetimeRaw[8] == 0){                      // day
                $day = $datetimeRaw[9];
            }
            else{
                $day = substr($datetimeRaw,8, 2);
                //echo $day;
            }
            $datetime = $month."/".$day."/".$year." ".substr($datetimeRaw,11, 5);   // "XX/XX/20XX XX:00"
            
            
            
            $weatherarray =  $hourly->weather;				// in case of singular or multiple weather reports
            if (sizeof($weatherarray) == 1){
                $weather = $hourly->weather[0]->main;			// ex. $weather = "Drizzle"
            }
            else {
                for($i=0; $i<count($weatherarray); $i++){
                    $weather = $hourly->weather[$i]->main;
                    break;
                    //$weather = $weather.", ".$w;     		// ex. $weather = "Drizzle, Mist, ...
                }
            }
            
        
            $stmt = $mysqli ->prepare("insert into weather (weather, temperature, windspeed, datetime) values (?, ?, ?, ?)");
            if(!$stmt){
                printf("Query prep failed: %s\n", $mysqli ->error);
                exit;
            }
            $stmt-> bind_param('sdds', $weather, $temperature, $windspeed, $datetime);
            $stmt->execute();
            $stmt->close();
        }
    }
    $checker = $checker+0.5;
}


?>

</body>
</html>