<?php


	// Returns all the transaction created by the customer 
	$feedbacks = [

		['id' => 1, 'user_id' => 1, 'comments' => 'Iphone has been broken'],
		['id' => 2, 'user_id' => 2, 'comments' => 'Computer was best buy'],
		['id' => 3, 'user_id' => 1, 'comments' => 'Microphone was not working']
	];

	echo(json_encode($feedbacks));
?>