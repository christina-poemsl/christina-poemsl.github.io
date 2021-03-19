for filepath in $1/*; do
    
    filename=$(basename $filepath "cm.jpg")

    if [ $filename != "thumb.jpg" ]; then
        
        width=$(echo $filename | cut -d"x" -f2)
        height=$((echo $filename | cut -d"x" -f1) | cut -d"_" - -f4)

        new_width=$(expr 600 \* $width / 140)

        convert "$filepath[($new_width)x]" $filepath

    fi

done
