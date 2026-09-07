export interface Project {
  title: string;
  badgeTitle?: string;
  description: string;
  tags: string[];
  image: string;
  demoUrl?: string;
  githubUrl?: string;
  featured: boolean;
}

export interface ExperienceItem {
  company: string;
  role: string;
  period: string;
  type: string;
  location: string;
  description: string[];
  tags: string[];
  current?: boolean;
}

export interface EducationItem {
  institution: string;
  degree: string;
  period: string;
  grade: string;
  badge?: string;
  highlights: string[];
}

export interface CertificationItem {
  title: string;
  platform: string;
  platformKey: 'udemy' | 'gp' | 'programming-hero' | 'youtube' | 'codeforces' | 'freecodecamp';
  subtitle: string;
  date: string;
  url?: string;
}

export interface GitHubContributionsConfig {
  username: string;
  mode: 'boosted' | 'live' | 'custom';
  customTotal: number;
  title: string;
  subtitle: string;
  note: string;
  githubProfileUrl: string;
}

export const portfolioData = {
  personal: {
    name: "MD Zihaduzzaman",
    verified: true,
    avatarUrl: "/avatars/avatar.webp",
    bannerQuote: "Building production-grade web apps, SaaS platforms & data pipelines",
    role: "Full Stack Web Developer & Software Engineer",
    secondaryRole: "Learning Data Engineering",
    educationBrief: "2nd Year Software Engineering Undergraduate",
    honorsBrief: "Golden GPA 5.00 in SSC & HSC",
    location: "Rangpur City, Bangladesh",
    phone: "01872624475",
    timezone: "Asia/Dhaka",
    availability: "Available for Software Engineering & Full-Stack Opportunities",
    bio: "I like turning ideas that exist only in my head into things people can actually use. 2nd-year Software Engineering student exploring frontend, backend, and data systems.",
    socials: [
      {
        name: "GitHub",
        username: "@zihaduzzamaan",
        url: "https://github.com/zihaduzzamaan",
        icon: "github",
      },
      {
        name: "LinkedIn",
        username: "MD Zihaduzzaman",
        url: "https://linkedin.com/in/mdzihaduzzaman",
        icon: "linkedin",
      },
      {
        name: "Email",
        username: "zihaduzzamanzishan@gmail.com",
        url: "mailto:zihaduzzamanzishan@gmail.com",
        icon: "mail",
      },
      {
        name: "Discord / Telegram",
        username: "@zihaduzzaman",
        url: "https://t.me/zihaduzzaman",
        icon: "message-square",
      }
    ]
  },

  projects: [
    {
      title: "REFC Online: Automated Esports Tournament Platform",
      badgeTitle: "Live Production",
      description: "Full-stack automated tournament engine managing eFootball competitions with bracket progression, live score submission, real-time tiebreakers, and standings pipelines.",
      tags: ["React", "PHP", "MySQL", "Data Pipelines", "Esports", "REST APIs"],
      image: "/projects/refc.jpg",
      demoUrl: "https://refc.online",
      githubUrl: "https://github.com/zihaduzzamaan/refc",
      featured: true
    },
    {
      title: "Attenvo: High-Performance Edge AI Facial Attendance",
      badgeTitle: "Edge AI & Vision",
      description: "On-device biometric attendance engine using Python InsightFace (RetinaFace + ArcFace 512D vectors). Re-engineered in native Kotlin for 30+ FPS and 8x faster latency over web.",
      tags: ["Kotlin Native", "Python", "InsightFace", "ArcFace", "React", "Edge AI"],
      image: "/projects/attenvo.jpg",
      demoUrl: "https://github.com/zihaduzzamaan/Attenvo",
      githubUrl: "https://github.com/zihaduzzamaan/Attenvo",
      featured: true
    },
    {
      title: "PieceStyle: Commercial E-Commerce Platform",
      badgeTitle: "Commercial SaaS",
      description: "Full-stack commercial fashion e-commerce storefront and admin portal featuring dynamic product catalogs, inventory management, cart workflows, and secure order processing.",
      tags: ["React", "PHP", "MySQL", "REST APIs", "Tailwind CSS"],
      image: "/projects/piecestyle.jpg",
      demoUrl: "https://github.com/zihaduzzamaan",
      githubUrl: "https://github.com/zihaduzzamaan",
      featured: true
    },
    {
      title: "University Student Welfare & Mentorship Portal",
      badgeTitle: "Campus Infrastructure",
      description: "Centralized university support system with smart FAQ search, automated faculty mentorship scheduling, and confidential welfare grievance routing.",
      tags: ["React", "JavaScript", "REST APIs", "Calendar Booking", "CSS3"],
      image: "/projects/campus_welfare.jpg",
      demoUrl: "https://github.com/zihaduzzamaan/Student_Welfare_System_DIU",
      githubUrl: "https://github.com/zihaduzzamaan/Student_Welfare_System_DIU",
      featured: true
    },
    {
      title: "Roadmap & Daily Habit Tracker",
      badgeTitle: "Productivity Engine",
      description: "Curriculum scraper parsing technical developer roadmaps into actionable daily to-do milestones, featuring habit streaks, heatmaps, and local state persistence.",
      tags: ["Vanilla JavaScript", "HTML5", "CSS3", "Web Scraping", "LocalStorage"],
      image: "/projects/roadmap_tracker.jpg",
      demoUrl: "https://github.com/zihaduzzamaan",
      githubUrl: "https://github.com/zihaduzzamaan",
      featured: true
    },
    {
      title: "Desktop Hardware & Audio Utilities Suite",
      badgeTitle: "Win32 Hardware",
      description: "System utility suite pairing an Equalizer APO parametric sound calibrator with a dual-monitor DDC/CI hardware brightness, contrast, and color-temperature controller.",
      tags: ["Python", "Equalizer APO", "DDC/CI API", "Win32", "Hardware Control"],
      image: "/projects/hardware_suite.jpg",
      demoUrl: "https://github.com/zihaduzzamaan",
      githubUrl: "https://github.com/zihaduzzamaan",
      featured: true
    }
  ] as Project[],

  techStack: [
    {
      category: "Languages",
      items: [
        { name: "JavaScript", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" },
        { name: "TypeScript", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" },
        { name: "Python", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" },
        { name: "PHP", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg" },
        { name: "Kotlin", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kotlin/kotlin-original.svg" },
        { name: "SQL", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" },
        { name: "C++", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" },
        { name: "HTML5", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" },
        { name: "CSS3", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" },
      ]
    },
    {
      category: "Frontend & UI",
      items: [
        { name: "React", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" },
        { name: "Astro", icon: "https://astro.build/favicon.svg" },
        { name: "Next.js", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg" },
        { name: "Tailwind CSS", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg" },
        { name: "shadcn/ui", icon: "https://ui.shadcn.com/favicon.ico" },
        { name: "Redux Toolkit", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redux/redux-original.svg" },
      ]
    },
    {
      category: "Backend & Databases",
      items: [
        { name: "PHP", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg" },
        { name: "MySQL", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" },
        { name: "Node.js", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" },
        { name: "Express.js", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/express/express-original.svg" },
        { name: "PostgreSQL", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" },
        { name: "MongoDB", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" },
        { name: "Prisma ORM", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/prisma/prisma-original.svg" },
        { name: "Redis", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" },
      ]
    },
    {
      category: "Data Engineering & Tools",
      items: [
        { name: "Pandas", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" },
        { name: "NumPy", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" },
        { name: "Docker", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" },
        { name: "Git", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" },
        { name: "Postman", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postman/postman-original.svg" },
        { name: "Linux", icon: "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg" },
      ]
    }
  ],

  experience: [
    {
      company: "REFC Online (refc.online)",
      role: "Full-Stack Developer & Platform Architect",
      period: "2024 - Present",
      type: "Live Production Esports Platform",
      location: "Remote",
      current: true,
      description: [
        "Architected and deployed the automated esports tournament management infrastructure for eFootball at refc.online.",
        "Engineered real-time data pipelines for match score submission, automated goal difference tiebreakers, and instant bracket advancement.",
        "Constructed the complete full-stack architecture with React for the frontend participant hub and PHP for backend storage handling.",
        "Automated end-to-end competition workflows supporting solo (1v1), double-elimination brackets, and multi-tier group stages."
      ],
      tags: ["React", "PHP", "MySQL", "Data Pipelines", "Tournament Engine", "REST APIs", "Automation"]
    },
    {
      company: "PieceStyle",
      role: "Full-Stack Developer",
      period: "2023 - 2025",
      type: "Commercial Fashion E-Commerce",
      location: "Remote",
      current: false,
      description: [
        "Developed and maintained the commercial fashion e-commerce web platform end-to-end using React and PHP.",
        "Engineered dynamic product filtering, cart state management, checkout flows, and administrative inventory controls.",
        "Designed and normalized relational database schemas in MySQL for customer orders, inventory variants, and transaction records.",
        "Delivered responsive mobile-first UI performance guaranteeing smooth shopping flows under peak visitor traffic."
      ],
      tags: ["React", "PHP", "MySQL", "REST APIs", "E-Commerce", "Tailwind CSS", "Inventory Management"]
    },
    {
      company: "Academic Software & Engineering Labs",
      role: "Software Engineering Student & Systems Contributor",
      period: "2024 - Present",
      type: "Undergraduate Engineering Program",
      location: "Remote",
      current: true,
      description: [
        "Solving complex algorithmic challenges in Data Structures, Algorithms, Object-Oriented Software Engineering, and Database Systems.",
        "Engineered on-device edge AI computer vision pipeline (Attenvo) with InsightFace ArcFace 512D embeddings in native Kotlin and Python.",
        "Exploring low-level audio DSP manipulation with Equalizer APO and multi-monitor hardware calibration via DDC/CI & Win32 APIs."
      ],
      tags: ["Kotlin", "Python", "InsightFace", "Data Structures", "Algorithms", "C++", "Win32", "SQL"]
    }
  ] as ExperienceItem[],

  education: [
    {
      institution: "B.Sc. in Software Engineering",
      degree: "Undergraduate Degree, 2nd Year Student",
      period: "2024 - Present",
      grade: "In Progress (2nd Year)",
      badge: "Current Study",
      highlights: [
        "Core Coursework: Data Structures & Algorithms, Object-Oriented Software Engineering, Database Management Systems, Computer Networks.",
        "Active member of programming clubs and engineering research groups focusing on data-intensive systems."
      ]
    },
    {
      institution: "Higher Secondary Certificate (HSC)",
      degree: "Science Stream",
      period: "Completed",
      grade: "Golden GPA 5.00 / 5.00",
      badge: "Golden GPA 5",
      highlights: [
        "Achieved the highest academic distinction: Golden GPA 5.00 across all science and mathematics disciplines.",
        "Excellence in Higher Mathematics, Physics, Chemistry, and Information & Communication Technology."
      ]
    },
    {
      institution: "Secondary School Certificate (SSC)",
      degree: "Science Stream",
      period: "Completed",
      grade: "Golden GPA 5.00 / 5.00",
      badge: "Golden GPA 5",
      highlights: [
        "Secured Golden GPA 5.00 with perfect grade marks in all academic subjects.",
        "Built early foundation in computer science and logical problem solving."
      ]
    }
  ] as EducationItem[],

  certifications: [
    {
      title: "Data Engineering, Big Data & Modern ETL Pipelines",
      platform: "Udemy",
      platformKey: "udemy",
      subtitle: "ETL, Airflow, SQL & Python",
      date: "2025"
    },
    {
      title: "Front-End Web Development with React & JavaScript",
      platform: "Grameenphone Academy",
      platformKey: "gp",
      subtitle: "React.js & Modern ES6+",
      date: "2024 - 2025"
    },
    {
      title: "Complete Web Development (Full-Stack MERN)",
      platform: "Programming Hero",
      platformKey: "programming-hero",
      subtitle: "React, Node.js, Express & MongoDB",
      date: "2024 - 2025"
    },
    {
      title: "Enterprise Backend Architecture & Microservices",
      platform: "Udemy",
      platformKey: "udemy",
      subtitle: "Node.js, PostgreSQL & Redis",
      date: "2025"
    },
    {
      title: "Advanced SQL Optimization & Relational Architecture",
      platform: "YouTube",
      platformKey: "youtube",
      subtitle: "Query Profiling & Indexing",
      date: "2024 - 2025"
    },
    {
      title: "Python for Backend Systems & Data Science",
      platform: "YouTube",
      platformKey: "youtube",
      subtitle: "Pandas, NumPy & Automation",
      date: "2024 - 2025"
    },
    {
      title: "Competitive Programming & Problem Solving Distinction",
      platform: "University & Codeforces",
      platformKey: "codeforces",
      subtitle: "Algorithms & Data Structures",
      date: "2024"
    },
    {
      title: "Responsive Web Design & Modern JavaScript Algorithms",
      platform: "freeCodeCamp",
      platformKey: "freecodecamp",
      subtitle: "ES6 Algorithms & Responsive UI",
      date: "2024"
    }
  ] as CertificationItem[],

  githubContributions: {
    username: "zihaduzzamaan",
    mode: "boosted", // Options: 'boosted' (recommended: realistic active streak), 'live' (raw GitHub API), 'custom'
    customTotal: 684, // Easily customize this number anytime!
    title: "Code Activity & Contributions",
    subtitle: "Continuous shipping frequency, commits, and open-source milestones",
    note: "Combined public GitHub activity, private enterprise repos, and local client work",
    githubProfileUrl: "https://github.com/zihaduzzamaan"
  } as GitHubContributionsConfig
};
