# Title
Jenkins script I use in my projects and spend some time researching.</br>
</br>
# Dependencies (jenkins_pipeline.py)<br>
OS: Ubuntu 16.04 Xenial</br>
Script to download the pipeline PNG from Jenkins Blue Ocean latest Branch</br>
```
sudo apt-get install chromium-chromedriver
sudo pip install Pillow
sudo pip install selenium
sudo pip install PyVirtualDisplay
```
# Dependencies (emailext_template.jelly)
OS: CentOS7</br>
Template that will send a nice formated email resume to the handlers of the project.</br>
```
mkdir /var/lib/jenkins/email-templates
On the Jenkinsfile with emailext:
--> body: '${JELLY_SCRIPT,template="emailext_template"}'
```
# Dependencies (Jenkinsfile.template)
OS: CentOS7</br>
Jenkinsfile DSL pipeline integration with: Jira, Gitlab and Email-ext</br>
```
Remove the template and add it in the root of your repository
```
# TODO</br>
</br>
