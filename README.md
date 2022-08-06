# VulnX 🕷️
![vulnx](./vulnxicon.png)
### CMS-Detector, Vulnerability Scanner, exploiter & An intelligent bot auto shell injector. 

### install:
  ###### install packages.
  - pip install -r ./requirements.txt
  ###### before_script:
  - pip install flake8
  ###### stop the build if there are Python syntax errors or undefined names
  - flake8 . --count --select=E901,E999,F821,F822,F823 --show-source --statistics
  ###### exit-zero treats all errors as warnings.  The GitHub editor is 127 chars wide
  - flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
### script:
  ###### run this command to grabber all informations, and apply the vunerabilites search
  - python3 vulnx.py -u isetso.rnu.tn --cms all -t3 --web-info --exploit
  ###### show list dorks & search example for blaze dork 5 page of google search & output the results to logs/Dorks/getTime()
  - python3 vulnx.py -l all -D blaze -n 5 --output logs/

### Docker Documentation.
##### Welcome to the vulnx DOCKER documentation. The vulnx DOCKER documentation is generated as a rule of usage docker.
##### You can build docker-image & run container for no problem of comptability:
 ````docker build -t vulnx ./docker/````
 
 ````docker run -it --name vulnx vulnx:latest -u http://prisma.id````

