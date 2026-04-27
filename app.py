import os
import json
from flask import Flask

# Declare static local var
string = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Shin Thant Phyo — AI Engineer</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style> 
        *, *::before, *::after {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --bg-primary: #0a0a0b;
            --bg-secondary: #111113;
            --bg-card: #16161a;
            --bg-card-hover: #1c1c21;
            --text-primary: #e8e8ed;
            --text-secondary: #9494a0;
            --text-muted: #5a5a6e;
            --accent: #6c63ff;
            --accent-light: #8b83ff;
            --accent-glow: rgba(108, 99, 255, 0.15);
            --accent-green: #34d399;
            --accent-blue: #60a5fa;
            --accent-orange: #fb923c;
            --accent-pink: #f472b6;
            --border: #22222a;
            --border-light: #2a2a35;
            --radius: 12px;
            --radius-lg: 20px;
            --transition: 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }

        html {
            scroll-behavior: smooth;
            scrollbar-width: thin;
            scrollbar-color: var(--accent) var(--bg-secondary);
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            line-height: 1.7;
            overflow-x: hidden;
        }

        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-track { background: var(--bg-secondary); }
        ::-webkit-scrollbar-thumb { background: var(--accent); border-radius: 3px; }

        /* Navigation */
        .nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            padding: 0 2rem;
            transition: var(--transition);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            background: rgba(10, 10, 11, 0.8);
            border-bottom: 1px solid transparent;
        }

        .nav.scrolled {
            border-bottom-color: var(--border);
        }

        .nav-inner {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 72px;
        }

        .nav-logo {
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text-primary);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .nav-logo .dot {
            width: 8px;
            height: 8px;
            background: var(--accent);
            border-radius: 50%;
            display: inline-block;
            animation: pulse-dot 2s ease-in-out infinite;
        }

        @keyframes pulse-dot {
            0%, 100% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.3); }
        }

        .nav-links {
            display: flex;
            gap: 0.25rem;
            list-style: none;
        }

        .nav-links a {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.875rem;
            font-weight: 500;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            transition: var(--transition);
            position: relative;
        }

        .nav-links a:hover, .nav-links a.active {
            color: var(--text-primary);
            background: var(--accent-glow);
        }

        .nav-toggle {
            display: none;
            flex-direction: column;
            gap: 5px;
            cursor: pointer;
            background: none;
            border: none;
            padding: 4px;
        }

        .nav-toggle span {
            width: 22px;
            height: 2px;
            background: var(--text-primary);
            border-radius: 2px;
            transition: var(--transition);
        }

        .nav-toggle.open span:nth-child(1) { transform: rotate(45deg) translate(5px, 5px); }
        .nav-toggle.open span:nth-child(2) { opacity: 0; }
        .nav-toggle.open span:nth-child(3) { transform: rotate(-45deg) translate(5px, -5px); }

        /* Hero Section */
        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            padding: 2rem;
        }

        .hero-bg {
            position: absolute;
            inset: 0;
            overflow: hidden;
        }

        .hero-bg::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(ellipse at 30% 50%, var(--accent-glow) 0%, transparent 50%),
                        radial-gradient(ellipse at 70% 50%, rgba(52, 211, 153, 0.05) 0%, transparent 50%);
            animation: hero-bg-rotate 30s linear infinite;
        }

        @keyframes hero-bg-rotate {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .grid-overlay {
            position: absolute;
            inset: 0;
            background-image:
                linear-gradient(rgba(108, 99, 255, 0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(108, 99, 255, 0.03) 1px, transparent 1px);
            background-size: 60px 60px;
            mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
            -webkit-mask-image: radial-gradient(ellipse at center, black 30%, transparent 70%);
        }

        .hero-content {
            text-align: center;
            position: relative;
            z-index: 1;
            max-width: 800px;
        }

        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.4rem 1rem;
            background: var(--accent-glow);
            border: 1px solid rgba(108, 99, 255, 0.2);
            border-radius: 100px;
            font-size: 0.8rem;
            font-weight: 500;
            color: var(--accent-light);
            margin-bottom: 2rem;
            animation: fadeInUp 0.8s ease-out;
        }

        .hero-badge .status-dot {
            width: 6px;
            height: 6px;
            background: var(--accent-green);
            border-radius: 50%;
            animation: pulse-dot 2s ease-in-out infinite;
        }

        .hero-name {
            font-size: clamp(2.5rem, 7vw, 5rem);
            font-weight: 800;
            letter-spacing: -0.03em;
            line-height: 1.1;
            margin-bottom: 1.5rem;
            animation: fadeInUp 0.8s ease-out 0.1s both;
        }

        .hero-name .gradient-text {
            background: linear-gradient(135deg, var(--accent-light), var(--accent-green));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .hero-title {
            font-size: clamp(1rem, 2.5vw, 1.35rem);
            color: var(--text-secondary);
            font-weight: 400;
            margin-bottom: 2.5rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            animation: fadeInUp 0.8s ease-out 0.2s both;
        }

        .hero-actions {
            display: flex;
            gap: 1rem;
            justify-content: center;
            flex-wrap: wrap;
            animation: fadeInUp 0.8s ease-out 0.3s both;
        }

        .btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 0.8rem 1.75rem;
            border-radius: 10px;
            font-size: 0.9rem;
            font-weight: 600;
            text-decoration: none;
            cursor: pointer;
            transition: var(--transition);
            border: none;
            font-family: inherit;
        }

        .btn-primary {
            background: var(--accent);
            color: white;
            box-shadow: 0 0 20px rgba(108, 99, 255, 0.3);
        }

        .btn-primary:hover {
            background: var(--accent-light);
            box-shadow: 0 0 30px rgba(108, 99, 255, 0.5);
            transform: translateY(-2px);
        }

        .btn-secondary {
            background: var(--bg-card);
            color: var(--text-primary);
            border: 1px solid var(--border);
        }

        .btn-secondary:hover {
            background: var(--bg-card-hover);
            border-color: var(--border-light);
            transform: translateY(-2px);
        }

        .hero-scroll-indicator {
            position: absolute;
            bottom: 2rem;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 0.5rem;
            color: var(--text-muted);
            font-size: 0.75rem;
            animation: bounce 2s ease-in-out infinite;
        }

        .scroll-line {
            width: 1px;
            height: 40px;
            background: linear-gradient(to bottom, var(--accent), transparent);
        }

        @keyframes bounce {
            0%, 100% { transform: translateX(-50%) translateY(0); }
            50% { transform: translateX(-50%) translateY(8px); }
        }

        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Sections */
        .section {
            padding: 6rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-header {
            margin-bottom: 4rem;
        }

        .section-label {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.8rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--accent-light);
            margin-bottom: 1rem;
        }

        .section-label::before {
            content: '';
            width: 20px;
            height: 2px;
            background: var(--accent);
            border-radius: 2px;
        }

        .section-title {
            font-size: clamp(1.75rem, 4vw, 2.5rem);
            font-weight: 700;
            letter-spacing: -0.02em;
            color: var(--text-primary);
        }

        .section-desc {
            color: var(--text-secondary);
            margin-top: 1rem;
            max-width: 600px;
            font-size: 1.05rem;
        }

        /* About Section */
        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }

        .about-image-wrapper {
            position: relative;
        }

        .about-image {
            width: 100%;
            aspect-ratio: 4/5;
            border-radius: var(--radius-lg);
            overflow: hidden;
            position: relative;
            background: var(--bg-card);
            border: 1px solid var(--border);
        }

        .about-image svg {
            width: 100%;
            height: 100%;
        }

        .about-image-decoration {
            position: absolute;
            top: -12px;
            right: -12px;
            width: 100%;
            height: 100%;
            border: 2px solid var(--accent);
            border-radius: var(--radius-lg);
            opacity: 0.2;
            z-index: -1;
        }

        .about-text h3 {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }

        .about-text p {
            color: var(--text-secondary);
            margin-bottom: 1.25rem;
            font-size: 0.95rem;
        }

        .about-stats {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 1.5rem;
            margin-top: 2rem;
            padding-top: 2rem;
            border-top: 1px solid var(--border);
        }

        .stat-item {
            text-align: center;
        }

        .stat-number {
            font-size: 1.75rem;
            font-weight: 800;
            color: var(--accent-light);
            font-family: 'JetBrains Mono', monospace;
        }

        .stat-label {
            font-size: 0.75rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 0.25rem;
        }

        /* Skills Section */
        .skills-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
            gap: 1.5rem;
        }

        .skill-category {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 2rem;
            transition: var(--transition);
        }

        .skill-category:hover {
            border-color: var(--border-light);
            background: var(--bg-card-hover);
            transform: translateY(-4px);
        }

        .skill-category-icon {
            width: 48px;
            height: 48px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.25rem;
            font-size: 1.25rem;
        }

        .skill-category-icon.frontend { background: rgba(108, 99, 255, 0.15); }
        .skill-category-icon.backend { background: rgba(52, 211, 153, 0.15); }
        .skill-category-icon.tools { background: rgba(251, 146, 60, 0.15); }
        .skill-category-icon.other { background: rgba(244, 114, 182, 0.15); }

        .skill-category h3 {
            font-size: 1.1rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }

        .skill-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .skill-tag {
            padding: 0.35rem 0.85rem;
            background: var(--bg-primary);
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 0.8rem;
            color: var(--text-secondary);
            font-weight: 500;
            transition: var(--transition);
        }

        .skill-tag:hover {
            border-color: var(--accent);
            color: var(--accent-light);
            background: var(--accent-glow);
        }

        /* Education Section */
        .timeline {
            position: relative;
            padding-left: 2rem;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, var(--accent), var(--border), transparent);
        }

        .timeline-item {
            position: relative;
            padding-bottom: 3rem;
            padding-left: 2rem;
        }

        .timeline-item:last-child {
            padding-bottom: 0;
        }

        .timeline-dot {
            position: absolute;
            left: -2rem;
            top: 0.25rem;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--accent);
            border: 3px solid var(--bg-primary);
            transform: translateX(-5px);
        }

        .timeline-date {
            display: inline-block;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--accent-light);
            background: var(--accent-glow);
            padding: 0.25rem 0.75rem;
            border-radius: 6px;
            margin-bottom: 0.75rem;
            font-family: 'JetBrains Mono', monospace;
        }

        .timeline-item h3 {
            font-size: 1.2rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }

        .timeline-item h4 {
            font-size: 0.95rem;
            font-weight: 500;
            color: var(--text-secondary);
            margin-bottom: 0.75rem;
        }

        .timeline-item p {
            color: var(--text-muted);
            font-size: 0.9rem;
            line-height: 1.7;
        }

        /* Projects Section */
        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
            gap: 1.5rem;
        }

        .project-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            overflow: hidden;
            transition: var(--transition);
            display: flex;
            flex-direction: column;
        }

        .project-card:hover {
            border-color: var(--border-light);
            transform: translateY(-6px);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }

        .project-image {
            width: 100%;
            height: 200px;
            overflow: hidden;
            position: relative;
        }

        .project-image svg {
            width: 100%;
            height: 100%;
        }

        .project-overlay {
            position: absolute;
            inset: 0;
            background: linear-gradient(to bottom, transparent 50%, var(--bg-card));
        }

        .project-content {
            padding: 1.5rem;
            flex: 1;
            display: flex;
            flex-direction: column;
        }

        .project-type {
            font-size: 0.7rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--accent-light);
            margin-bottom: 0.5rem;
        }

        .project-content h3 {
            font-size: 1.15rem;
            font-weight: 700;
            margin-bottom: 0.75rem;
        }

        .project-content p {
            color: var(--text-secondary);
            font-size: 0.875rem;
            margin-bottom: 1.25rem;
            flex: 1;
        }

        .project-tech {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-bottom: 1.25rem;
        }

        .project-tech span {
            padding: 0.25rem 0.65rem;
            background: var(--bg-primary);
            border-radius: 6px;
            font-size: 0.7rem;
            font-weight: 500;
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
        }

        .project-links {
            display: flex;
            gap: 0.75rem;
        }

        .project-links a {
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
            font-size: 0.8rem;
            color: var(--text-secondary);
            text-decoration: none;
            font-weight: 500;
            transition: var(--transition);
        }

        .project-links a:hover {
            color: var(--accent-light);
        }

        /* Experience Section */
        .experience-list {
            display: flex;
            flex-direction: column;
            gap: 1.5rem;
        }

        .experience-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 2rem;
            transition: var(--transition);
        }

        .experience-card:hover {
            border-color: var(--border-light);
            background: var(--bg-card-hover);
        }

        .experience-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1rem;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .experience-header h3 {
            font-size: 1.15rem;
            font-weight: 700;
        }

        .experience-header h4 {
            font-size: 0.95rem;
            font-weight: 500;
            color: var(--accent-light);
            margin-top: 0.15rem;
        }

        .experience-period {
            font-size: 0.8rem;
            color: var(--text-muted);
            font-family: 'JetBrains Mono', monospace;
            white-space: nowrap;
        }

        .experience-card ul {
            list-style: none;
            padding: 0;
        }

        .experience-card li {
            color: var(--text-secondary);
            font-size: 0.9rem;
            padding: 0.3rem 0;
            padding-left: 1.25rem;
            position: relative;
        }

        .experience-card li::before {
            content: '▹';
            position: absolute;
            left: 0;
            color: var(--accent);
        }

        /* Contact Section */
        .contact-section {
            text-align: center;
        }

        .contact-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
            margin-top: 3rem;
        }

        .contact-card {
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 2rem;
            text-align: center;
            transition: var(--transition);
            text-decoration: none;
            color: inherit;
            display: block;
        }

        .contact-card:hover {
            border-color: var(--accent);
            background: var(--accent-glow);
            transform: translateY(-4px);
        }

        .contact-icon {
            width: 56px;
            height: 56px;
            border-radius: 16px;
            background: var(--accent-glow);
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.25rem;
            font-size: 1.5rem;
            transition: var(--transition);
        }

        .contact-card:hover .contact-icon {
            background: var(--accent);
            transform: scale(1.1);
        }

        .contact-card h3 {
            font-size: 1rem;
            font-weight: 600;
            margin-bottom: 0.35rem;
        }

        .contact-card p {
            color: var(--text-secondary);
            font-size: 0.85rem;
        }

        /* Footer */
        .footer {
            border-top: 1px solid var(--border);
            padding: 3rem 2rem;
            text-align: center;
        }

        .footer p {
            color: var(--text-muted);
            font-size: 0.85rem;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 1.5rem;
        }

        .footer-links a {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 0.85rem;
            transition: var(--transition);
        }

        .footer-links a:hover {
            color: var(--accent-light);
        }

        /* Scroll Animations */
        .reveal {
            opacity: 0;
            transform: translateY(40px);
            transition: opacity 0.8s ease-out, transform 0.8s ease-out;
        }

        .reveal.visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Mobile Responsive */
        @media (max-width: 768px) {
            .nav-links {
                position: fixed;
                top: 72px;
                left: 0;
                right: 0;
                background: rgba(10, 10, 11, 0.95);
                backdrop-filter: blur(20px);
                flex-direction: column;
                padding: 1rem;
                gap: 0.25rem;
                border-bottom: 1px solid var(--border);
                transform: translateY(-100%);
                opacity: 0;
                pointer-events: none;
                transition: var(--transition);
            }

            .nav-links.open {
                transform: translateY(0);
                opacity: 1;
                pointer-events: all;
            }

            .nav-links a {
                padding: 0.75rem 1rem;
            }

            .nav-toggle {
                display: flex;
            }

            .about-grid {
                grid-template-columns: 1fr;
                gap: 2rem;
            }

            .about-image-wrapper {
                max-width: 300px;
                margin: 0 auto;
            }

            .about-stats {
                grid-template-columns: repeat(3, 1fr);
                gap: 1rem;
            }

            .skills-container {
                grid-template-columns: 1fr;
            }

            .projects-grid {
                grid-template-columns: 1fr;
            }

            .hero-name {
                font-size: clamp(2rem, 10vw, 3.5rem);
            }

            .section {
                padding: 4rem 1.25rem;
            }

            .experience-header {
                flex-direction: column;
            }
        }

        /* Floating particles */
        .particles-container {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
        }
    </style>
</head>
<body>

    <!-- Navigation -->
    <nav class="nav" id="navbar">
        <div class="nav-inner">
            <a href="#hero" class="nav-logo">
                <span class="dot"></span>
                alex.dev
            </a>
            <ul class="nav-links" id="navLinks">
                <li><a href="#about">About</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#experience">Experience</a></li>
                <li><a href="#education">Education</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <button class="nav-toggle" id="navToggle" aria-label="Toggle menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </nav>

    <!-- Hero -->
    <section class="hero" id="hero">
        <div class="hero-bg">
            <div class="grid-overlay"></div>
        </div>
        <div class="hero-content">
            <div class="hero-badge">
                <span class="status-dot"></span>
                Available for opportunities
            </div>
            <h1 class="hero-name">
                Hi, I'm <span class="gradient-text">John Doe</span>
            </h1>
            <p class="hero-title">
                Full-Stack Software Engineer crafting scalable systems and delightful user experiences with clean, performant code.
            </p>
            <div class="hero-actions">
                <a href="#projects" class="btn btn-primary">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                    View Projects
                </a>
                <a href="#contact" class="btn btn-secondary">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                    Get in Touch
                </a>
            </div>
        </div>
        <div class="hero-scroll-indicator">
            <span>Scroll</span>
            <div class="scroll-line"></div>
        </div>
    </section>

    <!-- About -->
    <section class="section" id="about">
        <div class="section-header reveal">
            <div class="section-label">About Me</div>
            <h2 class="section-title">Passionate about building things that live on the internet</h2>
        </div>
        <div class="about-grid">
            <div class="about-image-wrapper reveal">
                <div class="about-image">
                    <svg viewBox="0 0 400 500" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="avatarGrad" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" style="stop-color:#6c63ff;stop-opacity:0.3"/>
                                <stop offset="100%" style="stop-color:#34d399;stop-opacity:0.1"/>
                            </linearGradient>
                        </defs>
                        <rect width="400" height="500" fill="#16161a"/>
                        <circle cx="200" cy="180" r="70" fill="url(#avatarGrad)" stroke="#6c63ff" stroke-width="1.5" opacity="0.8"/>
                        <circle cx="200" cy="180" r="55" fill="none" stroke="#6c63ff" stroke-width="0.5" opacity="0.4"/>
                        <text x="200" y="188" text-anchor="middle" fill="#6c63ff" font-family="Inter" font-size="48" font-weight="700">AC</text>
                        <rect x="80" y="280" width="240" height="200" rx="16" fill="#111113" stroke="#22222a" stroke-width="1"/>
                        <text x="200" y="320" text-anchor="middle" fill="#9494a0" font-family="JetBrains Mono" font-size="12">&lt;softwareEngineer&gt;</text>
                        <text x="200" y="345" text-anchor="middle" fill="#e8e8ed" font-family="JetBrains Mono" font-size="11">{</text>
                        <text x="120" y="370" fill="#6c63ff" font-family="JetBrains Mono" font-size="10">  name: "Alex Chen",</text>
                        <text x="120" y="390" fill="#34d399" font-family="JetBrains Mono" font-size="10">  role: "Full-Stack",</text>
                        <text x="120" y="410" fill="#fb923c" font-family="JetBrains Mono" font-size="10">  location: "San Francisco",</text>
                        <text x="120" y="430" fill="#f472b6" font-family="JetBrains Mono" font-size="10">  passions: ["Code", "Design"]</text>
                        <text x="200" y="455" text-anchor="middle" fill="#e8e8ed" font-family="JetBrains Mono" font-size="11">}</text>
                        <text x="200" y="480" text-anchor="middle" fill="#9494a0" font-family="JetBrains Mono" font-size="12">&lt;/softwareEngineer&gt;</text>
                    </svg>
                </div>
                <div class="about-image-decoration"></div>
            </div>
            <div class="about-text reveal">
                <h3>A developer who loves turning complex problems into simple, beautiful solutions.</h3>
                <p>
                    I'm a software engineer based in San Francisco with 5+ years of experience building web applications and distributed systems. I specialize in React, TypeScript, Node.js, and cloud-native architectures.
                </p>
                <p>
                    Currently, I'm focused on building accessible, human-centered products at a fast-growing startup. Previously, I worked on large-scale data platforms and microservices architectures at leading tech companies.
                </p>
                <p>
                    When I'm not coding, you'll find me hiking in the Bay Area, contributing to open-source projects, or writing about software architecture on my blog.
                </p>
                <div class="about-stats">
                    <div class="stat-item">
                        <div class="stat-number" data-count="5">0</div>
                        <div class="stat-label">Years Exp.</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number" data-count="30">0</div>
                        <div class="stat-label">Projects</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-number" data-count="12">0</div>
                        <div class="stat-label">Open Source</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills -->
    <section class="section" id="skills">
        <div class="section-header reveal">
            <div class="section-label">Skills & Tools</div>
            <h2 class="section-title">Technologies I work with</h2>
            <p class="section-desc">A curated list of the tools and technologies I use to bring products to life.</p>
        </div>
        <div class="skills-container">
            <div class="skill-category reveal">
                <div class="skill-category-icon frontend">⚡</div>
                <h3>Frontend</h3>
                <div class="skill-tags">
                    <span class="skill-tag">React</span>
                    <span class="skill-tag">TypeScript</span>
                    <span class="skill-tag">Next.js</span>
                    <span class="skill-tag">Vue.js</span>
                    <span class="skill-tag">Tailwind CSS</span>
                    <span class="skill-tag">GraphQL</span>
                    <span class="skill-tag">Redux</span>
                    <span class="skill-tag">Framer Motion</span>
                </div>
            </div>
            <div class="skill-category reveal">
                <div class="skill-category-icon backend">🔧</div>
                <h3>Backend</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Node.js</span>
                    <span class="skill-tag">Python</span>
                    <span class="skill-tag">Go</span>
                    <span class="skill-tag">PostgreSQL</span>
                    <span class="skill-tag">MongoDB</span>
                    <span class="skill-tag">Redis</span>
                    <span class="skill-tag">REST APIs</span>
                    <span class="skill-tag">gRPC</span>
                </div>
            </div>
            <div class="skill-category reveal">
                <div class="skill-category-icon tools">☁️</div>
                <h3>DevOps & Cloud</h3>
                <div class="skill-tags">
                    <span class="skill-tag">AWS</span>
                    <span class="skill-tag">Docker</span>
                    <span class="skill-tag">Kubernetes</span>
                    <span class="skill-tag">CI/CD</span>
                    <span class="skill-tag">Terraform</span>
                    <span class="skill-tag">GitHub Actions</span>
                    <span class="skill-tag">Linux</span>
                </div>
            </div>
            <div class="skill-category reveal">
                <div class="skill-category-icon other">🎨</div>
                <h3>Other</h3>
                <div class="skill-tags">
                    <span class="skill-tag">Figma</span>
                    <span class="skill-tag">Git</span>
                    <span class="skill-tag">Agile/Scrum</span>
                    <span class="skill-tag">System Design</span>
                    <span class="skill-tag">Testing</span>
                    <span class="skill-tag">Documentation</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Experience -->
    <section class="section" id="experience">
        <div class="section-header reveal">
            <div class="section-label">Work Experience</div>
            <h2 class="section-title">Where I've worked</h2>
            <p class="section-desc">My professional journey across startups and enterprise environments.</p>
        </div>
        <div class="experience-list">
            <div class="experience-card reveal">
                <div class="experience-header">
                    <div>
                        <h3>Senior Software Engineer</h3>
                        <h4>TechNova Inc.</h4>
                    </div>
                    <span class="experience-period">Jan 2023 — Present</span>
                </div>
                <ul>
                    <li>Lead a team of 6 engineers building a real-time collaboration platform serving 50K+ daily active users</li>
                    <li>Architected microservices migration reducing deployment time by 70% and improving system reliability to 99.9%</li>
                    <li>Implemented WebSocket-based live editing features with CRDT conflict resolution</li>
                    <li>Mentored 3 junior engineers through structured code reviews and pair programming sessions</li>
                </ul>
            </div>
            <div class="experience-card reveal">
                <div class="experience-header">
                    <div>
                        <h3>Software Engineer</h3>
                        <h4>DataStream Labs</h4>
                    </div>
                    <span class="experience-period">Mar 2021 — Dec 2022</span>
                </div>
                <ul>
                    <li>Built and maintained high-throughput data pipelines processing 2M+ events per day using Apache Kafka</li>
                    <li>Developed a real-time analytics dashboard using React, D3.js, and GraphQL with sub-second query response</li>
                    <li>Optimized PostgreSQL queries reducing average response time from 800ms to 120ms</li>
                    <li>Designed and implemented CI/CD pipelines with automated testing achieving 95% code coverage</li>
                </ul>
            </div>
            <div class="experience-card reveal">
                <div class="experience-header">
                    <div>
                        <h3>Junior Software Engineer</h3>
                        <h4>CloudBridge Solutions</h4>
                    </div>
                    <span class="experience-period">Jun 2019 — Feb 2021</span>
                </div>
                <ul>
                    <li>Developed RESTful APIs in Node.js and Express serving 10K+ requests per minute</li>
                    <li>Built responsive web applications using React and TypeScript for client-facing products</li>
                    <li>Participated in on-call rotation handling production incidents and implementing post-mortem fixes</li>
                </ul>
            </div>
        </div>
    </section>

    <!-- Education -->
    <section class="section" id="education">
        <div class="section-header reveal">
            <div class="section-label">Education</div>
            <h2 class="section-title">Academic background</h2>
        </div>
        <div class="timeline">
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <span class="timeline-date">2017 — 2019</span>
                <h3>Master of Science in Computer Science</h3>
                <h4>Stanford University</h4>
                <p>Specialized in Distributed Systems and Machine Learning. Thesis on "Optimizing Consensus Algorithms for Geo-Distributed Databases." GPA: 3.9/4.0</p>
            </div>
            <div class="timeline-item reveal">
                <div class="timeline-dot"></div>
                <span class="timeline-date">2013 — 2017</span>
                <h3>Bachelor of Science in Computer Science</h3>
                <h4>University of California, Berkeley</h4>
                <p>Dean's List all semesters. Vice President of the ACM Student Chapter. Completed capstone project building a peer-to-peer file sharing system.</p>
            </div>
        </div>
    </section>

    <!-- Projects -->
    <section class="section" id="projects">
        <div class="section-header reveal">
            <div class="section-label">Featured Projects</div>
            <h2 class="section-title">Things I've built</h2>
            <p class="section-desc">A selection of projects that showcase my skills and passion for building.</p>
        </div>
        <div class="projects-grid">
            <div class="project-card reveal">
                <div class="project-image">
                    <svg viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="projGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" style="stop-color:#6c63ff;stop-opacity:0.4"/>
                                <stop offset="100%" style="stop-color:#34d399;stop-opacity:0.2"/>
                            </linearGradient>
                        </defs>
                        <rect width="600" height="200" fill="#111113"/>
                        <rect x="30" y="20" width="200" height="160" rx="12" fill="#16161a" stroke="#22222a" stroke-width="1"/>
                        <rect x="45" y="40" width="100" height="8" rx="4" fill="#6c63ff" opacity="0.6"/>
                        <rect x="45" y="58" width="140" height="6" rx="3" fill="#22222a"/>
                        <rect x="45" y="74" width="120" height="6" rx="3" fill="#22222a"/>
                        <rect x="45" y="96" width="160" height="40" rx="8" fill="#6c63ff" opacity="0.15"/>
                        <circle cx="250" cy="100" r="60" fill="url(#projGrad1)" opacity="0.5"/>
                        <rect x="270" y="20" width="300" height="160" rx="12" fill="#16161a" stroke="#22222a" stroke-width="1"/>
                        <rect x="295" y="40" width="80" height="8" rx="4" fill="#34d399" opacity="0.6"/>
                        <rect x="295" y="60" width="250" height="6" rx="3" fill="#22222a"/>
                        <rect x="295" y="76" width="200" height="6" rx="3" fill="#22222a"/>
                        <rect x="295" y="92" width="220" height="6" rx="3" fill="#22222a"/>
                        <rect x="295" y="116" width="100" height="30" rx="8" fill="#34d399" opacity="0.15"/>
                        <rect x="410" y="116" width="100" height="30" rx="8" fill="#6c63ff" opacity="0.15"/>
                    </svg>
                    <div class="project-overlay"></div>
                </div>
                <div class="project-content">
                    <span class="project-type">Full-Stack App</span>
                    <h3>FlowBoard — Real-time Collaboration Platform</h3>
                    <p>A Notion-like collaborative workspace with real-time editing, rich text formatting, and team workspaces. Handles concurrent edits using CRDT algorithms.</p>
                    <div class="project-tech">
                        <span>React</span>
                        <span>TypeScript</span>
                        <span>Node.js</span>
                        <span>PostgreSQL</span>
                        <span>WebSocket</span>
                    </div>
                    <div class="project-links">
                        <a href="#">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                            Live Demo
                        </a>
                        <a href="#">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
                            Source Code
                        </a>
                    </div>
                </div>
            </div>
            <div class="project-card reveal">
                <div class="project-image">
                    <svg viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="projGrad2" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" style="stop-color:#fb923c;stop-opacity:0.4"/>
                                <stop offset="100%" style="stop-color:#f472b6;stop-opacity:0.2"/>
                            </linearGradient>
                        </defs>
                        <rect width="600" height="200" fill="#111113"/>
                        <rect x="30" y="20" width="540" height="160" rx="12" fill="#16161a" stroke="#22222a" stroke-width="1"/>
                        <rect x="50" y="40" width="60" height="8" rx="4" fill="#fb923c" opacity="0.6"/>
                        <rect x="50" y="60" width="200" height="100" rx="8" fill="url(#projGrad2)" opacity="0.3"/>
                        <polyline points="70,140 110,120 150,130 190,90 230,95" fill="none" stroke="#fb923c" stroke-width="2" opacity="0.6"/>
                        <circle cx="190" cy="90" r="4" fill="#fb923c" opacity="0.8"/>
                        <circle cx="230" cy="95" r="4" fill="#f472b6" opacity="0.8"/>
                        <rect x="300" y="40" width="250" height="30" rx="8" fill="#22222a"/>
                        <rect x="300" y="80" width="250" height="30" rx="8" fill="#22222a"/>
                        <rect x="300" y="120" width="250" height="30" rx="8" fill="#22222a"/>
                        <rect x="315" y="50" width="60" height="10" rx="5" fill="#fb923c" opacity="0.4"/>
                        <rect x="315" y="90" width="80" height="10" rx="5" fill="#f472b6" opacity="0.4"/>
                        <rect x="315" y="130" width="50" height="10" rx="5" fill="#34d399" opacity="0.4"/>
                    </svg>
                    <div class="project-overlay"></div>
                </div>
                <div class="project-content">
                    <span class="project-type">Data Platform</span>
                    <h3>PipelineX — Data Processing Engine</h3>
                    <p>A high-performance data pipeline tool that processes millions of events daily with real-time analytics dashboards and anomaly detection.</p>
                    <div class="project-tech">
                        <span>Python</span>
                        <span>Kafka</span>
                        <span>Redis</span>
                        <span>D3.js</span>
                        <span>Docker</span>
                    </div>
                    <div class="project-links">
                        <a href="#">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                            Live Demo
                        </a>
                        <a href="#">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
                            Source Code
                        </a>
                    </div>
                </div>
            </div>
            <div class="project-card reveal">
                <div class="project-image">
                    <svg viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg">
                        <defs>
                            <linearGradient id="projGrad3" x1="0%" y1="0%" x2="100%" y2="100%">
                                <stop offset="0%" style="stop-color:#60a5fa;stop-opacity:0.4"/>
                                <stop offset="100%" style="stop-color:#6c63ff;stop-opacity:0.2"/>
                            </linearGradient>
                        </defs>
                        <rect width="600" height="200" fill="#111113"/>
                        <rect x="150" y="20" width="300" height="160" rx="12" fill="#16161a" stroke="#22222a" stroke-width="1"/>
                        <rect x="170" y="35" width="260" height="20" rx="6" fill="#22222a"/>
                        <circle cx="190" cy="45" r="5" fill="#fb923c" opacity="0.6"/>
                        <circle cx="206" cy="45" r="5" fill="#f472b6" opacity="0.6"/>
                        <circle cx="222" cy="45" r="5" fill="#34d399" opacity="0.6"/>
                        <rect x="170" y="65" width="120" height="100" rx="8" fill="url(#projGrad3)" opacity="0.2"/>
                        <text x="230" y="120" text-anchor="middle" fill="#60a5fa" font-family="JetBrains Mono" font-size="14">{ }</text>
                        <rect x="310" y="65" width="120" height="45" rx="8" fill="#22222a"/>
                        <rect x="325" y="80" width="60" height="6" rx="3" fill="#60a5fa" opacity="0.4"/>
                        <rect x="325" y="94" width="80" height="6" rx="3" fill="#22222a"/>
                        <rect x="310" y="120" width="120" height="45" rx="8" fill="#22222a"/>
                        <rect x="325" y="135" width="70" height="6" rx="3" fill="#6c63ff" opacity="0.4"/>
                        <rect x="325" y="149" width="90" height="6" rx="3" fill="#22222a"/>
                    </svg>
                    <div class="project-overlay"></div>
                </div>
                <div class="project-content">
                    <span class="project-type">Open Source</span>
                    <h3>DevKit — Developer Toolkit CLI</h3>
                    <p>A powerful CLI tool for scaffolding projects, managing environments, and automating common development workflows. 2K+ GitHub stars.</p>
                    <div class="project-tech">
                        <span>Go</span>
                        <span>CLI</span>
                        <span>Templates</span>
                        <span>GitHub API</span>
                    </div>
                    <div class="project-links">
                        <a href="#">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
                            GitHub
                        </a>
                        <a href="#">
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                            Docs
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact -->
    <section class="section contact-section" id="contact">
        <div class="section-header reveal" style="text-align: center;">
            <div class="section-label" style="justify-content: center;">Get in Touch</div>
            <h2 class="section-title">Let's work together</h2>
            <p class="section-desc" style="margin: 1rem auto 0; max-width: 500px;">
                I'm always interested in hearing about new projects and opportunities. Whether you have a question or just want to say hi, feel free to reach out!
            </p>
        </div>
        <div class="contact-grid">
            <a href="mailto:alex@example.com" class="contact-card reveal">
                <div class="contact-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6c63ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
                </div>
                <h3>Email</h3>
                <p>alex@example.com</p>
            </a>
            <a href="https://github.com" target="_blank" class="contact-card reveal">
                <div class="contact-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6c63ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"/></svg>
                </div>
                <h3>GitHub</h3>
                <p>github.com/alexchen</p>
            </a>
            <a href="https://linkedin.com" target="_blank" class="contact-card reveal">
                <div class="contact-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6c63ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
                </div>
                <h3>LinkedIn</h3>
                <p>linkedin.com/in/alexchen</p>
            </a>
            <a href="https://twitter.com" target="_blank" class="contact-card reveal">
                <div class="contact-icon">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#6c63ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 4s-.7 2.1-2 3.4c1.6 10-9.4 17.3-18 11.6 2.2.1 4.4-.6 6-2C3 15.5.5 9.6 3 5c2.2 2.6 5.6 4.1 9 4-.9-4.2 4-6.6 7-3.8 1.1 0 3-1.2 3-1.2z"/></svg>
                </div>
                <h3>Twitter / X</h3>
                <p>@alexchendev</p>
            </a>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-links">
            <a href="#about">About</a>
            <a href="#skills">Skills</a>
            <a href="#experience">Experience</a>
            <a href="#projects">Projects</a>
            <a href="#contact">Contact</a>
        </div>
        <p>Designed & built by Alex Chen · © 2024</p>
    </footer>

    <script>
        // Navigation scroll effect
        const navbar = document.getElementById('navbar');
        const navToggle = document.getElementById('navToggle');
        const navLinks = document.getElementById('navLinks');

        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Mobile nav toggle
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('open');
            navLinks.classList.toggle('open');
        });

        // Close mobile nav on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('open');
                navLinks.classList.remove('open');
            });
        });

        // Active nav link highlighting
        const sections = document.querySelectorAll('section[id]');
        const navLinksList = navLinks.querySelectorAll('a');

        function updateActiveNav() {
            const scrollPos = window.scrollY + 150;
            sections.forEach(section => {
                const top = section.offsetTop;
                const height = section.offsetHeight;
                const id = section.getAttribute('id');
                if (scrollPos >= top && scrollPos < top + height) {
                    navLinksList.forEach(a => a.classList.remove('active'));
                    const activeLink = navLinks.querySelector(`a[href="#${id}"]`);
                    if (activeLink) activeLink.classList.add('active');
                }
            });
        }

        window.addEventListener('scroll', updateActiveNav);

        // Scroll reveal animations
        const revealElements = document.querySelectorAll('.reveal');

        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        });

        revealElements.forEach(el => revealObserver.observe(el));

        // Counter animation
        const statNumbers = document.querySelectorAll('.stat-number[data-count]');

        const counterObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const target = entry.target;
                    const count = parseInt(target.getAttribute('data-count'));
                    let current = 0;
                    const increment = count / 40;
                    const suffix = count >= 10 ? '+' : '+';

                    const timer = setInterval(() => {
                        current += increment;
                        if (current >= count) {
                            current = count;
                            clearInterval(timer);
                        }
                        target.textContent = Math.floor(current) + suffix;
                    }, 30);

                    counterObserver.unobserve(target);
                }
            });
        }, { threshold: 0.5 });

        statNumbers.forEach(el => counterObserver.observe(el));

        // Smooth scroll for all anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
    </script>
</body>
</html>
"""

# Create a Flask app
app = Flask(__name__)

# Create a dir or else router
@app.route('/')
def home():
    return(f"{string}")

if __name__ == '__main__':
    app.run('127.0.0.1', port=8080)