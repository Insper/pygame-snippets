ffmpeg -i $1 -pix_fmt rgb24 -r 10 -s ${3:-255x320} $2
