# ************************************************************
# Sequel Ace SQL dump
# Version 20095
#
# https://sequel-ace.com/
# https://github.com/Sequel-Ace/Sequel-Ace
#
# Host: localhost (MySQL 9.4.0)
# Database: testsqlai
# Generation Time: 2025-08-17 14:54:40 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
SET NAMES utf8mb4;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE='NO_AUTO_VALUE_ON_ZERO', SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table courses
# ------------------------------------------------------------

DROP TABLE IF EXISTS `courses`;

CREATE TABLE `courses` (
  `course_id` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(100) NOT NULL,
  `course_description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `duration_weeks` int NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `location` varchar(100) NOT NULL,
  `instructor_name` varchar(100) NOT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `max_students` int DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`course_id`),
  CONSTRAINT `chk_duration` CHECK ((`duration_weeks` > 0)),
  CONSTRAINT `chk_price` CHECK ((`price` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;

INSERT INTO `courses` (`course_id`, `course_name`, `course_description`, `duration_weeks`, `price`, `location`, `instructor_name`, `phone_number`, `email`, `start_date`, `end_date`, `max_students`, `is_active`, `created_at`, `updated_at`)
VALUES
	(1,'Webinar : AI Kickstarter for Beginners & Career Opportunities\n','Duration: 3 Hours\nFormat: Interactive (Lectures + Live Demos + Q&A)\n\nSession 1: AI Basics & Real-World Impact (45 Mins)\n1. Introduction (10 Mins)\nIcebreaker Poll: \"Why are you interested in AI?\" (Career change, skill upgrade, curiosity)\nSpeaker Intro + Success Stories (e.g., \"How a beginner landed an AI internship\")\n2. What is AI? (15 Mins)\nSimple Definition: \"AI = Machines doing human-like tasks\"\nFun Examples: TikTok filters, Spotify recommendations, spam filters\nAI Myths Busted (e.g., \"Will AI replace all jobs?\")\n3. How AI is Useful TODAY (15 Mins)\nTools You Can Use NOW:\nChatGPT (email drafting)\nGemini (research summaries)\nCanva AI (design)\nIndustries Hiring Beginners:\nMarketing (AI ads), Healthcare (chatbots), E-commerce (product recommendations)\n4. Live Demo (5 Mins)\n\"Turn your idea into an AI app in 2 mins\"\nBreak (15 Mins)\n\nSession 2: Your First AI Project & Skills to Learn (45 Mins)\n1. Build Your First AI Agent (15 Mins)\nZero-Coding Option: Customize a chatbot \nWith Coding (Simplified)\n2. Deploy & Share Your AI (10 Mins)\nFree hosting \n\"How to add AI projects to your resume\"\n3. Top 5 AI Jobs for Beginners (10 Mins)\nPrompt Engineer\nAI Data Analyst\nFreelance AI Consultant\nBonus: Companies hiring entry-level (IBM, Accenture, startups)\n4. Skills Roadmap (10 Mins)\n3-Month Plan: Beginner Course\nMonth 1: Python + ChatGPT\nMonth 2: Build 2 projects (e.g., resume parser, Twitter bot)\nMonth 3: Apply for internships\nBreak (15 Mins)\n\nSession 3: Monetize AI & Next Steps (45 Mins)\n1. Make Money with AI (15 Mins)\nSide Hustles:\nSell AI art (Etsy)\nFreelance (Fix businesses’ ChatGPT workflows)\nCase Study: *\"How a student made 5000/month with AI\"*\n2. Certificates & Resume (10 Mins)\nFree Certs: Google AI, Microsoft AI\n\"The \'AI Projects\' Section That Gets You Hired\"\n3. Ethics & Future (10 Mins)\nDark Side of AI: Deepfakes, job displacement\nHow to Stay Ahead: Lifelong learning\nQ&A (30 Mins)\nCareer Advice: \"How to switch from non-tech to AI?\"\nGiveaway: Free 1:1 career coaching for 3 attendees\n\n',1,999.00,'Online','Sivakumar','6362620391','email2sivakumarindia@gmail.com','2025-09-10','2025-09-11',100,1,'2025-08-17 20:00:41','2025-08-17 20:19:38'),
	(2,'AI Mastery: Advanced Techniques & Research\n\n','Duration: 8 Weekends (or 12 Weekdays) | Total Hours: 120 | Fee: ₹1,00,000\nPrerequisite:\nStrong Python + Intermediate ML/DL (or completion of AI Accelerator Course)\nBasic understanding of cloud platforms (AWS/GCP)\nOutcome:\nPublish a research paper (IEEE/arXiv) or deploy a scalable AI product\nCrack FAANG-level AI roles (₹15L+ avg salary for freshers)\n\nCourse Structure\nWeek 1-2: Advanced Deep Learning\nTopics:\nGenerative AI: Diffusion Models, GANs (Stable Diffusion, StyleGAN)\nReinforcement Learning: Q-Learning, PPO (OpenAI Gym)\nHands-on: Build a text-to-image generator (like MidJourney).\nWeek 3-4: AI Research & Optimization\nTopics:\nLLM Fine-Tuning: LoRA, Quantization (Llama 2, Mistral)\nModel Compression: Pruning, Distillation (TinyBERT)\nHands-on: Create a domain-specific ChatGPT (e.g., legal/finance bot).\nWeek 5-6: Scalable AI Systems\nTopics:\nDistributed Training: PyTorch Lightning, Ray\nMLOps at Scale: Kubernetes, MLflow, TFX\nHands-on: Deploy a multi-model inference pipeline (e.g., fraud detection + NLP).\nWeek 7-8: Research/Industry Project\n',8,80000.00,'Online','Sivakumar','6362620391','email2sivakumarindia@gmail.com','2025-08-01','2025-11-02',100,1,'2025-08-11 13:12:55','2025-08-17 20:19:40'),
	(3,'AI Accelerator: Intermediate to Industry-Ready\n','Duration: 8 Weekends (or 12 Weekdays) | Total Hours: 120 | Fee: ₹75,000\nPrerequisite: Python basics + understanding of ML concepts (or Beginner AI course)\nOutcome: Master advanced AI tools, build deployable solutions, and crack internships/jobs in AI/ML roles.\n\nCourse Structure\nWeek 1-2: Advanced Machine Learning\nTopics:\nFeature Engineering & Hyperparameter Tuning (GridSearchCV, AutoML)\nEnsemble Methods (Random Forest, XGBoost)\nHands-on: Kaggle-style competition (Top 3 winners get mentorship).\nWeek 3-4: Deep Learning Dive\nTopics:\nCNNs for Computer Vision (Transfer Learning with ResNet)\nNLP: Transformers, BERT, and Hugging Face pipelines\nHands-on: Build a sentiment analysis API with Flask.\nWeek 5-6: MLOps & Deployment\nTopics:\nModel Deployment (FastAPI, Docker, AWS SageMaker)\nMonitoring & CI/CD for ML models\nHands-on: Deploy a fraud detection model on the cloud.\nWeek 7-8: Industry Projects & Interviews\nTopics:\nCase Studies: How Swiggy/Zomato uses AI for recommendations\nMock Interviews: FAANG-style ML interview prep\nCapstone Project: End-to-end AI solution (e.g., document summarizer with user dashboard).\n\nKey Differentiators\n🔥 Advanced Tools: LangChain, LlamaIndex, Vertex AI\n🔥 Cloud Labs: AWS/GCP credits provided for projects\n🔥 Guaranteed Internships: Tie-ups with 50+ startups (Unpaid/Paid)\n🔥 Freelance Pipeline: Access to Upwork/Fiverr gigs (₹50k+ projects)\n\nBatch Options\nWeekend Batch (Sat-Sun, 5 hrs/day)\nWeekday Batch (Mon-Thu, 3 hrs/day)\nNext Cohort Starts: [Date]\nEarly Bird Discount: 10% off till [Date]\n\nWho Should Join?\nBE/BSc grads who know Python but lack industry projects.\nBeginners who completed the AI Kickstarter Course.\nProfessionals targeting AI Engineer/Data Scientist roles.\n\nSample Project Portfolio\nMedical Diagnosis Assistant (CNN + Flask)\nAI Resume Optimizer (NLP + GPT-4 API)\nSupply Chain Demand Predictor (Time Series Forecasting)\n',8,30000000.00,'Online','Sivakumar','6362620391','email2sivakumarindia@gmail.com','2025-08-01','2025-11-02',50,1,'2025-08-11 13:29:16','2025-08-17 20:19:41'),
	(4,'AI Kickstarter Course for Beginners','Duration: 8 Weekends (or 12 Weekdays) | Total Hours: 120 | Fee: ₹50,000\nEligibility: BE/BSc Graduates (No prior AI experience needed)\nOutcome: Build 4 AI projects, earn a certificate, and land internships/jobs.\n\nCourse Structure\nWeek 1-2: AI Foundations & Python Basics\nTopics:\nWhat is AI? Real-world applications (Healthcare, E-commerce, etc.)\nPython for AI (Syntax, Libraries: NumPy, Pandas)\nHands-on: Build a simple chatbot using Python.\nWeek 3-4: Machine Learning & Data\nTopics:\nSupervised vs. Unsupervised Learning\nData Cleaning & Visualization (Matplotlib, Seaborn)\nHands-on: Predict house prices using linear regression.\nWeek 5-6: Deep Learning & AI Tools\nTopics:\nNeural Networks (CNNs, RNNs)\nTensorFlow/Keras basics\nHands-on: Image classifier for cats/dogs.\nWeek 7-8: Projects & Career Prep\nTopics:\nDeploy AI models (Flask, Hugging Face)\nResume building + LinkedIn optimization\nCapstone Project: End-to-end AI app (e.g., resume screener).\n\nKey Features\n✅ Industry-Aligned Curriculum (NASSCOM AI certified)\n✅ 1:1 Mentorship (Weekly doubt sessions)\n✅ Placement Support (Resume reviews, mock interviews)\n✅ Freelance Guide (How to earn ₹20k+/month with AI gigs)\n',8,29000.00,'Online','Sivakumar','63626260391','email2sivakumarindia@gmail.com','2025-10-01','2026-02-01',100,1,'2025-08-11 12:43:17','2025-08-17 20:19:41');

/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table registrations
# ------------------------------------------------------------

DROP TABLE IF EXISTS `registrations`;

CREATE TABLE `registrations` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `student_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `student_phone_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `student_email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `course_id` int NOT NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `email` (`student_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

LOCK TABLES `registrations` WRITE;
/*!40000 ALTER TABLE `registrations` DISABLE KEYS */;

INSERT INTO `registrations` (`student_id`, `student_name`, `student_phone_number`, `student_email`, `course_id`)
VALUES
	(12,'Mani Batcha Boy','9632164873','test@ghtu.com',1),
	(14,'sidhaarthan','9600405729','meetsidhaarthan@gmail.com',1),
	(16,'namasivayam','96326832832','test@test.com',1),
	(17,'Selvaraj','9632164985','email2s@gmail.com',1),
	(22,'varalakshmi','918787563743','emai2sfa@gmail.com',1),
	(23,'Anil basha','983734748373','test@asdfasd.com',2),
	(25,'Ramchandran','98237478384','rams@dasf.com',1);

/*!40000 ALTER TABLE `registrations` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
