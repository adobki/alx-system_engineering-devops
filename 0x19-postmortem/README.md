# Incident Report of AirBnB Clone v4 Outage on 5/5/2023

###### ALX Software Engineering Course

###### _[Original article on Medium](https://medium.com/@adobki/incident-report-of-airbnb-clone-v4-outage-on-5-5-2023-a158dda64627)_

![](media/artwork_11235921_11104_sml.png)

_[Image by pch.vector](https://www.freepik.com/free-vector/tiny-people-examining-operating-system-error-warning-web-page-isolated-flat-illustration_11235921.htm#query=incident%20report&position=3&from_view=search&track=ais) on Freepik_

This is a postmortem (also known as **_incident report_**) of the global outage of the AirBnB Clone v4 website that occurred from the afternoon of Friday, the 5th of May, 2023 at 4:04PM (WAT), to the morning of Monday, 8th of May, 2023 at 2:00AM (WAT). The website was down completely due to a firewall configuration issue in the load balancer that disabled its internet access.



### Timeline
_(All times are in WAT/GMT+1 on the morning of Monday, 8th of May, 2023)_

* **12:12AM —** Outage was detected when on-call engineer noticed missing logs for the previous day. Daily logs are normally uploaded automatically from the web servers by 12:00AM.
* **12:14AM —** Engineer initially assumed it was a problem with his internet connection and checked that, then refreshed his view multiple times.
* **12:18AM —** He then realised it was a problem with the load balancer when he could neither connect to it via a secure shell (SSH) nor get a response from its IP address when pinged or website URL visited in a browser.
* **12:23AM —** He pinged and SSH’ed into all the web servers directly, one after the other and found that they were all functioning optimally.
* **12:29AM —** He parsed their logs and discovered that the last http request across all the servers was received from the load balancer at 4:04PM on Friday, 5th of May, 2023.
* **12:38AM —** Engineer escalated issue to his manager, and their final resolution was to destroy and redeploy the container housing the load balancer due to the time constraints, but this required further escalation.
* **01:00AM —** Emergency meeting was held with key players –several HODs (Cyber Security, Infrastructure, etc.), the engineer, his manager, etc.– to discourse and approve their recommended action.
* **01:45AM —** Meeting ended with approval given to the team to destroy and redeploy the load balancer’s container.
* **01:50AM —** Engineer backed up the container, then destroyed it. He redeployed a new one and configured it according to the previous load balancer’s specifications.
* **02:00AM —** On-call engineer opened the AirBnB Clone v4 website in his browser and confirmed that it was back online.



### Root Cause and Resolution
Further inspection of the backed-up container after disassembly and analysis revealed that it went offline due to an issue with its firewall’s configuration which was triggered during a maintenance operation carried out on the Friday afternoon. The maintenance person accidentally set a firewall rule to block all traffic (incoming and outgoing) and logged-off immediately, without noticing its impact.

A new load balancer server was reconfigured and deployed to replace the offline one. This ended the outage as the website was back online and available again on the internet globally. (See _**[Timeline](#timeline)**_ above for more details.)



### Corrective and Preventive Measures
1. [x] All server maintenance operations must be preceded and succeeded by specific tests to detect issues and ensure optimal states of performance before and after these operations.
2. [ ] Only highly-skilled personnel should be given the high levels of security clearance required to access the load balancer and other core services.
3. [x] Regular backups are done of all server containers so that any misconfiguration, breach, damage, etc. can be recovered from easily.
4. [x] Policies have been put in place to make future escalation paths shorter for container destruction and redeployment when the redeployment would be to the most recent container backup.
5. [x] A monitoring tool, Datadog, has been deployed to monitor and report servers’ statuses and operations so that issues can be detected in real-time and troubleshot promptly, as opposed to days later.


#
###### _[Original article on Medium](https://medium.com/@adobki/incident-report-of-airbnb-clone-v4-outage-on-5-5-2023-a158dda64627)_
