<?php
require 'database.php';

$years = range(2012,2015);
$months = range(1,12);
$day30s = range(1,30);
$day31s = range(1,31);
$day28s = range(1,28);
$dayLeaps = range(1,29);
$hours = range(0,23);
$minutes = range(0,59);
$url = array();
date_default_timezone_set("UTC");
foreach($years as $year){
foreach($months as $month){
    switch($month){
            case 1:
                foreach($day31s as $day31){
                        $date = $month."/".$day31."/".$year;
                        $dateforday = $year."-".$month."-".$day31;
                        $day = date('D',strtotime($dateforday));
                        $coordinatetmp = array();
                        $time = "00:00:00";
                        $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                        $data = json_decode(file_get_contents($add));
                        $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                        $warningcounts = substr_count(file_get_contents($add),'warnings');
                        $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                        for($i = 0; $i < sizeof($routeoption); $i++){
                            for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                array_push($coordinatetmp,$routeoption[$i][$j]);
                            }
                        }
                        $coordinateString = implode($coordinatetmp);
                        $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                        if(!$stmt){
                             printf("Query prep failed: %s\n", $mysqli ->error);
                            exit;
                        }
                        $datetime = $date." 00:00";
                        $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                        $stmt->execute();
                        $stmt->close();
                    }
                case 2:
                        foreach($day28s as $day28){
                            $date = $month."/".$day28."/".$year;
                            $dateforday = $year."-".$month."-".$day28;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                    
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                      
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
                case 3:
                   foreach($day31s as $day31){
                            $date = $month."/".$day31."/".$year;
                            $dateforday = $year."-".$month."-".$day31;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                      
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $coordinateString = implode($coordinatetmp);
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
                case 4:
                    foreach($day30s as $day30){
                            $date = $month."/".$day30."/".$year;
                            $dateforday = $year."-".$month."-".$day30;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                      
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $coordinateString = implode($coordinatetmp);
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
                case 5:
                    foreach($day31s as $day31){
                        $date = $month."/".$day31."/".$year;
                            $dateforday = $year."-".$month."-".$day31;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                    
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $coordinateString = implode($coordinatetmp);
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
                case 6:
                    foreach($day30s as $day30){
                        $date = $month."/".$day30."/".$year;
                            $dateforday = $year."-".$month."-".$day30;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
               
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $coordinateString = implode($coordinatetmp);
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
                case 7:
                    foreach($day31s as $day31){
                       $date = $month."/".$day31."/".$year;
                            $dateforday = $year."-".$month."-".$day31;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                     
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $coordinateString = implode($coordinatetmp);
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
                case 8:
                    foreach($day31s as $day31){
                        $date = $month."/".$day31."/".$year;
                            $dateforday = $year."-".$month."-".$day31;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                   
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $coordinateString = implode($coordinatetmp);
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
                case 9:
                    foreach($day30s as $day30){
                       $date = $month."/".$day30."/".$year;
                            $dateforday = $year."-".$month."-".$day30;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                 
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $coordinateString = implode($coordinatetmp);
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
                case 10:
                    foreach($day31s as $day31){
                        $date = $month."/".$day31."/".$year;
                            $dateforday = $year."-".$month."-".$day31;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                     
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $coordinateString = implode($coordinatetmp);
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
                case 11:
                    foreach($day30s as $day30){
                        $date = $month."/".$day30."/".$year;
                            $dateforday = $year."-".$month."-".$day30;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $coordinateString = implode($coordinatetmp);
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
                case 12:
                    foreach($day31s as $day31){
                        $date = $month."/".$day31."/".$year;
                            $dateforday = $year."-".$month."-".$day31;
                            $day = date('D',strtotime($dateforday));
                            $coordinatetmp = array();
                
                            $time = "00:00:00";
                            $add = "http://dev.virtualearth.net/REST/v1/Routes/Driving?wp.0=JohnHancockCenter,IL&wp.1=41.884276,-87.652300&dateTime=".$date."%20".$time."&optimize=timeWithTraffic&maxSolutions=1&routeAttributes=routePath&key=ApGGpVO4paSpEQFMfeUvO0r0c5FmkglSlJnJx712pulc-SmjuGG017PlS1Ba6xMY";
                 
                            $data = json_decode(file_get_contents($add));
                            $routeoption = $data -> resourceSets[0] -> resources[0] -> routePath -> line -> coordinates;
                            $warningcounts = substr_count(file_get_contents($add),'warnings');
                            $congestion = $data -> resourceSets[0] -> resources[0] -> trafficCongestion; //heavy, medium, mild
                            for($i = 0; $i < sizeof($routeoption); $i++){
                                for($j = 0; $j < sizeof($routeoption[$i]); $j++){
                                    array_push($coordinatetmp,$routeoption[$i][$j]);
                                }
                            }
                            $coordinateString = implode($coordinatetmp);
                            $stmt = $mysqli ->prepare("insert into congestion (congestion, warningcounts, routeoption, datetime, day) values (?, ?, ?, ?, ?)");
                            if(!$stmt){
                                 printf("Query prep failed: %s\n", $mysqli ->error);
                                exit;
                            }
                            $datetime = $date." 00:00";
                            $stmt-> bind_param('sisss', $congestion, $warningcounts, $coordinateString, $datetime, $day);
                            $stmt->execute();
                            $stmt->close();
                    }
    }
}
}


?>

