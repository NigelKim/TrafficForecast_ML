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

$pos2012 = strrpos($dataraw, "2012-") + 31;
$pos2013start = $pos2012+1;
$pos2013end = strrpos($dataraw, "2013-") + 31;
$pos2014start = $pos2013end+1;
$pos2014end = strrpos($dataraw, "2014-") + 31;
$pos2015start = $pos2014end+1;
$pos2015end = strrpos($dataraw, "2015-") + 31;

$data2012 = json_decode(substr($dataraw, 0, $pos2012)."]");
$data2013 = json_decode("[".substr($dataraw, $pos2013start, $pos2013end-$pos2013start)."]");
$data2014 = json_decode("[".substr($dataraw, $pos2014start, $pos2014end-$pos2014start)."]");
$data2015 = json_decode("[".substr($dataraw, $pos2015start, $pos2015end-$pos2015start)."]");


$yrArray = array();
array_push($yrArray, $data2012);
array_push($yrArray, $data2013);
array_push($yrArray, $data2014);
array_push($yrArray, $data2015);




//echo $data2012;
//echo $dataraw;

//$data = json_decode($dataraw);  //Fatal error: Allowed memory size of 134217728 bytes exhausted (tried to allocate 81 bytes)

//// if clear table
$stmt2 = $mysqli->prepare("truncate table weather");
$stmt2->execute();
$stmt2->close();

$checker = 2012;
//print_r($yrArray[2]);
foreach($yrArray as $yrData){
    echo " accessed ".$checker;
    foreach((array) $yrData as $hourly){
        //print_r($hourly);
    //for($i=0; $i<count($data); $i++){
        
        $temperature = (double) $hourly->main->temp;            // temperature in Kelvin
        $windspeed = (double) $hourly->wind->speed;             // wind speed in m/s
        
        $datetimeRaw = $hourly->dt_iso;     				    // date and time in "20XX-XX-XX XX:00:00 +0000 UTC"
        if (substr($datetimeRaw,11,2) == "00"){         // comment this out if we want to get ALL POSSIBLE HOURLY DATA.
                                                        // currently, only getting 00:00 data
            $year = substr($datetimeRaw,0, 4);                  // year
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
    $checker = $checker+1;
}


?>

</body>
</html>