INTEGER X,Y,Z
INPUT X,Y
IF(X >= 10 AND X <= 12 )
	AND(Y >= 8 AND Y<=11)
  THEN
	  Z = X / 2 * Y
	  		//正确的表述为：
	  		//Z = X / 7 * Y
  ELSE
  	  Z = X * Y
OUTPUT Z



INTEGER X,Y,Z
INPUT X,Y
IF(2 * X - Y >10)
		//正确的表述为：
		//IF(2 * X - Y > 18)
THEN
	Z = X / 2 * Y
ELSE
	Z = X* Y
OUTPUT Z


INTEGER X,Y,Z
INPUT X,Y
IF (X mod 4 =0 AND Y mod 6 =0)
 THEN 
 	Z = X / 2 * Y
 		//正确的表述为：
 		//Z = X/ 7 * Y
 ELSE
 	Z = X * Y
 OUTPUT Z