#!/bin/sh  
list_alldir(){  
    for file2 in `ls -a $1`  
    do  
        if [ x"$file2" != x"." -a x"$file2" != x".." ];then  
            if [ -d "$1/$file2" ];then  
                echo "$1/$file2"  
                list_alldir "$1/$file2"  
			else
				filename=$(ch2py "$file2" -s _)
				filename=${filename%_*}
				echo "$1/$file2 -> $1/$filename.png"
				mv "$1/$file2" "$1/$filename.png"
			fi  
        fi  
    done  
}  

testif() {
	if [ x"$test" = x"test" ];then
		echo "ok"
	else
		filename=$(ch2py "$1" -s _)
		echo $filename
	fi
}

#testif 测试
list_alldir .

