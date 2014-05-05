<?php

$allPaths = array ();

function d($p) {var_dump($p);}

function recursive ($currentItem, $stdin, $z, $currentPath = [])
{
	global $allPaths;
	
	$currentPath[] = $currentItem;
	
	// Remove current item from stdin (local var called like that)
	if( ($key = array_search($currentItem, $stdin)) !== false )
		unset ($stdin[$key]);
	array_values ($stdin);
	
	$possibleItems = array ();
	
	// Get all items / levenshtein(currentItem, for each in stdin) == 0
	foreach ($stdin as $item)
	{
		if (levenshtein ($currentItem, $item) == 1)
			$possibleItems[] = $item;
	}
	
	if ( empty($possibleItems) ) return;
	
	foreach ($possibleItems as $item)
	{
		if ($item == $z)
		{
			$currentPath[] = $z;
			$allPaths[] = $currentPath;
		}
		else
		{
			recursive ($item, $stdin, $z, $currentPath);
		}
	}
}

// Read stdin
$stdin = file ('PHP://stdin');
// OR
//$stdin = file('stdin.txt', FILE_IGNORE_NEW_LINES);
//

// Remove new lines
for ($i=0; $i<count($stdin); ++$i)
	$stdin[$i] = trim(preg_replace('/\s\s+/', ' ', $stdin[$i]));
	
// Get beginning and end
$a = array_shift ($stdin);
$z = array_shift ($stdin);

recursive ($a, $stdin, $z);

// Get minimum path
$path = $allPaths[0];
for ($i=1; $i<count($allPaths); ++$i)
{
	if (count($allPaths[$i]) < count($path))
		$path = $allPaths[$i];
}

// Write path
$path = implode ('->', $path);
echo $path;

?>