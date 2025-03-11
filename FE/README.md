#### 2025 Rihal Codestacker Challenge

# Shadow Watch Frontend

## Storyline

A criminal group has attacked the city's crime reporting systems. They have damaged security cameras, blocked radio signals, and cut phone lines. Because of this, police and citizens cannot report or track crimes properly. City officials need a new Crime Reporting System (CRS) as soon as possible to keep everyone safe.

Your mission? Develop an interactive and responsive web application to serve as the new CRS. Your application should provide a map-based crime reporting and tracking system, allowing citizens to reporAt incidents while enabling authorities to monitor active crime zones efficiently.

## Challenge Levels

#### Level 1 (30 points): Basic Crime Map & Data Handling

The first step is to build a map-based crime reporting dashboard.

1.  Fetch crime data from a provided JSON file.
2.  Display crime reports as special drop pins on the map.
3.  On hovering or clicking a crime pin, show a popup card with the following details: - **Report Details:** Information related to the crime. - **Crime Type:** Assault, Robbery, Homicide, Kidnapping. - **Report Date & Time:** When the crime was reported. - **Report Status:** Pending, En Route, On Scene, Under Investigation, Resolved. -
    **Bonus**: Implement category-based filtering, allowing users to show/hide specific crime types.

#### Level 2 (40 points): Crime Reporting Form & Submission

Enable citizens to report crimes via an interactive form.

1.  Add a "Report Crime" button that opens a form when clicked.
2.  The form should include:
    - **Report Details:** Text input.
    - **Crime Type:** Select input (Assault, Robbery, Homicide, Kidnapping).
    - **National ID:** Number input (should accept only numbers).
    - **Crime Location:** Two fields for Longitude and Latitude, where users manually enter coordinates.
3.  On submission, automatically set:
    - **Status:** "Pending"
    - **Report Date & Time:** Current timestamp (YYYY-MM-DD-HH-MM format)
4.  Display newly submitted reports dynamically on the map.

**Bonus:** Validate form inputs.

> NOTE : Keeping data in local storage is accepted

#### Level 3 (20 points): Enhanced Crime Location Selection & UI Enhancements

Improve the crime reporting experience by making location selection more interactive.

1.  Add a `Select Crime Location` button that allows users to click on
    the map to drop a location pin instead of manually entering
    coordinates.
2.  Display a confirm button below the map to finalize the selection.
3.  Implement a search bar to find crimes by type, date, or ID.

**Bonus:** Implement local storage or simple backend API to persist data.

#### Bonus Task: Deployment & Mobile Optimization

Showcase your ability to take your project to production!

- Deploy the application (e.g., Vercel, Netlify, DigitalOcean, or Firebase).
- Ensure full mobile responsiveness.
- Implement PWA (Progressive Web App) support for offline access.

**Submission for Bonus Task:**

- Provide a public URL to the deployed application.
- Submit a README with deployment details and instructions.
- Optionally, include a video demo showcasing your application.

## Submission Guidelines

**Levels 1 & 2 (Basic UI & Features)**

- Submit the project as a GitHub repository.
- Include a README explaining how to set up and run the project.
- Provide a link to the deployed project (if applicable).

**Level 3 (Advanced Features & Enhancements)**

- Include well-structured code with comments.
- Provide a demo or screenshots of core features.

**Bonus Task (Deployment & Mobile Optimization)**

- Share deployment details.
- Explain how to run the project locally and in production.

Evaluation Criteria

- Functionality: Does the app meet all requirements at each level?
- UI/UX: Is the interface intuitive and user-friendly?
- Code Quality: Is the code clean, modular, and well-documented?
- Innovation: Are there creative features beyond the core requirements?
- Scalability: Can the project be extended or integrated into a larger
  system?

## Final Note

Bonus points will be awarded for well-structured, scalable, and production-ready solutions. Feel free to add extra features that enhance usability, security, and performance.

**Good luck, and happy coding! 🚀**
