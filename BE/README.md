# { BE Rihal Codestacker Challenge 2025 }

## Background

Crime City is under siege—rising crime and failing trust have left the community on edge. To turn things around, officials launched a Crime Management System, enabling real-time crime case reporting and faster police response. Now, they need your help!

Now, the officals need your expertise to develop a robust backend API system to efficiently manage their growing crimes data and improve response times.

## Problem statement

Your task is to develop a backend server system (API) for a crime case management platform.This system will allow registered users, such as police officers and investigators, to create, update, and monitor criminal cases while generating detailed reports.The system should provide a seamless experience for users while ensuring data integrity, security, scalability and reliability.

**Think you have what it takes? Step up, take on the challenge, and help restore peace to the people of Crime City! 🚔💻**

## 📌 Overall Requirements and APIs

1. ...

## Technical Requirements:

1. Use [git](https://git-scm.com/) as your version control system.

2. Your code MUST be on github. Your submission should include the link to the repository.

3. Use whatever language and framework you desire.

4. Database: You are required to use [PostgreSQL](https://www.postgresql.org/). You can use [ElephantSQL](https://www.elephantsql.com/) (FREE) or the [docker instance](https://hub.docker.com/_/postgres) if you decided to dockerize your project (check bouns challenges below).

5. File Storage: You can use any storage you want (e.g., [MinIO](https://min.io/), [Google Cloud Storage](https://cloud.google.com/storage))

## 💡 Bonus Challenges:

Want to stand out from the competition? These extra challenges give you the chance to showcase your skills beyond the basics. While not required, completing them can enhance your chances of winning by demonstrating your capability to tackle real-world BE application like scalability, performance, and reliability. Feel free to undertake any or all of them as you wish, and  show what you’re capable of!

### 1. 🔄 Long Polling for Evidence Hard Delete

Your task is to implement a long polling mechanism that allows admins to initiate ,monitor ,and track the hard deletion of evidence. This ensures they receive real-time updates on the status of their deletion requests, improving transparency and efficiency in the system.

**Key Requirements** :

1. Develop an API endpoint that allows admins to initiate the hard deletion of evidence. This endpoint should accept  the evidence ID and user authentication details.

2. Develop another endpoint that allows admins to check the status of the deletion process using long polling. Keep the connection open until the deletion is complete or a timeout occurs, and ensure that the admin receives updates on the deletion progress, including statuses such as "In Progress," "Completed," and "Failed." The client should be able to manage these status updates appropriately

### 2. 📨 Email Notification System for Crime Awareness

Your task is to develop an email notification system that will send timely updates to residents of [] regarding the status of crime in their area. This system should inform users about new crime incidents, updates on ongoing cases, and important safety alerts. By keeping the community informed, we aim to foster a safer environment and encourage proactive engagement among residents

**Key Requirements** :

1. Choose an email service provider (e.g., SendGrid, Mailgun) and integrate it into your application to facilitate the sending of email notifications.

2. Create a mechanism to trigger email notifications based on specific events, such as new crime incidents reported in the City,updates or changes to existing cases (e.g., status updates, new evidence) and community awwarness and safety alerts.

### 3. 💬 Case Commenting 

Your task is to implement a commenting feature for crime cases that enables assignees to add, retrieve, and delete comments associated with specific cases. This will help officers and investigators document their thoughts, share insights, and provide updates on ongoing investigations

**Key Requirements** :

1. Develop endpoints for adding comments to a specific case, retrieving all comments for a case, and deleting comments made by the assignees.

2. Ensure each comment is timestamped and linked to the user who made it for accountability and traceability.

3. Ensure comments are between 5 and 150 characters. Return "Comment must be at least 5 characters long." if under 5 characters, and "Comment cannot exceed 150 characters." if over 150 characters. Restrict comments to alphanumeric characters, spaces, and basic punctuation. Return "Comment contains invalid characters. Please use only letters, numbers, and basic punctuation." for disallowed characters, and "HTML tags are not allowed in comments." if HTML tags are detected.

4. Implement rate limiting to restrict the number of comments a user can post within a certain timeframe (e.g., no more than 5 comments per minute).

### 4. 🚀 Deployment

1. **Dockerization & Containerization**: Dockerize your project using [Docker](https://www.docker.com/) and Docker Compose to run your application.

2. **Cloud Deployment**: Deploy your application on any cloud platform and provide a **link to your deployed application**.
   - Submit your **Dockerfile**, deployment scripts, and a **README** explaining how to run and deploy the project.

## NOTE

1. This is a purely backend challenge! You should only create an API server without any front-end component.

---

# Unleash Your Creativity - Enjoy ✨💡 !
