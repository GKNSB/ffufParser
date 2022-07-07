## ffufParser
Parse ffuf results to eliminate false positive. I usually run ffuf for multiple urls like so:
```
azz=0; for url in $(< /root/Bounties/asdf/urls.txt); do ffuf -w /root/Tools/MyWordlists/common.txt -r -c -o /root/Bounties/asdf/ffufOutput/$azz.csv -of csv -timeout 5 -se -mc all -fc 300-399,400,401,403,404,429 -H "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20190101 Firefox/77.0" -ac -u $url"FUZZ"; azz=$((azz+1)); done
```
This results in a directory of multiple .csv files that have the ffuf results. This is a helper script that takes such a results directory as input and goes through all results in order to identify false positives and filter them out (for instance custom error page for non-existent page responding with 200 to everything).

```
usage: ffufParser.py [-h] ffufOutputDir output

I parse ffuf output files

positional arguments:
  ffufOutputDir  Ffuf output directory containing .csv files
  output         Output file location

optional arguments:
  -h, --help     show this help message and exit
```