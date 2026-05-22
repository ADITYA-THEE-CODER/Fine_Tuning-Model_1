# =========================================
# STEP 9: Create Bigger Training Dataset
# =========================================

data = [

    {"text": "User: Create exam notes on chess\nAssistant: Chess is a strategy board game played on an 8x8 board."},

    {"text": "User: Create exam notes on football\nAssistant: Football is a team sport where players try to score goals."},

    {"text": "User: Create exam notes on basketball\nAssistant: Basketball is a sport where two teams try to score points by shooting a ball into a hoop."},

    {"text": "User: Create exam notes on cricket\nAssistant: Cricket is a bat-and-ball sport played between two teams of eleven players."},

    {"text": "User: Create exam notes on tennis\nAssistant: Tennis is a racket sport played between two players or two teams."},

    {"text": "User: Create exam notes on volleyball\nAssistant: Volleyball is a team sport where players hit a ball over a net."},

    {"text": "User: Create exam notes on hockey\nAssistant: Hockey is a sport played using sticks to hit a puck or ball into a goal."},

    {"text": "User: Create exam notes on badminton\nAssistant: Badminton is a racket sport played using a shuttlecock over a net."},

    {"text": "User: Create exam notes on swimming\nAssistant: Swimming is an individual or team racing sport performed in water."},

    {"text": "User: Create exam notes on athletics\nAssistant: Athletics includes sports like running, jumping, and throwing events."},

    {"text": "User: Create exam notes on biology\nAssistant: Biology is the scientific study of living organisms and life processes."},

    {"text": "User: Create exam notes on physics\nAssistant: Physics studies matter, energy, motion, and forces in the universe."},

    {"text": "User: Create exam notes on chemistry\nAssistant: Chemistry studies substances, reactions, and chemical properties."},

    {"text": "User: Create exam notes on mathematics\nAssistant: Mathematics is the study of numbers, quantities, and patterns."},

    {"text": "User: Create exam notes on history\nAssistant: History studies past events, civilizations, and human development."},

    {"text": "User: Create exam notes on geography\nAssistant: Geography studies Earth's landscapes, environments, and populations."},

    {"text": "User: Create exam notes on computer science\nAssistant: Computer science studies computation, algorithms, and programming."},

    {"text": "User: Create exam notes on machine learning\nAssistant: Machine learning enables computers to learn patterns from data."},

    {"text": "User: Create exam notes on artificial intelligence\nAssistant: Artificial intelligence focuses on creating systems that mimic human intelligence."},

    {"text": "User: Create exam notes on deep learning\nAssistant: Deep learning uses neural networks with multiple layers for learning patterns."},

    {"text": "User: Create exam notes on neural networks\nAssistant: Neural networks are AI systems inspired by the structure of the human brain."},

    {"text": "User: Create exam notes on Python\nAssistant: Python is a high-level programming language known for simplicity and readability."},

    {"text": "User: Create exam notes on Java\nAssistant: Java is an object-oriented programming language widely used in software development."},

    {"text": "User: Create exam notes on C++\nAssistant: C++ is a powerful programming language used in systems and game development."},

    {"text": "User: Create exam notes on data science\nAssistant: Data science involves extracting insights from structured and unstructured data."},

    {"text": "User: Create exam notes on SQL\nAssistant: SQL is a language used for managing and querying databases."},

    {"text": "User: Create exam notes on databases\nAssistant: Databases store and organize information electronically."},

    {"text": "User: Create exam notes on cloud computing\nAssistant: Cloud computing delivers computing services over the internet."},

    {"text": "User: Create exam notes on cybersecurity\nAssistant: Cybersecurity protects systems, networks, and data from digital attacks."},

    {"text": "User: Create exam notes on networking\nAssistant: Networking connects computers and devices for communication and data sharing."},

    {"text": "User: Create exam notes on operating systems\nAssistant: Operating systems manage computer hardware and software resources."},

    {"text": "User: Create exam notes on Linux\nAssistant: Linux is an open-source operating system widely used in servers and development."},

    {"text": "User: Create exam notes on Git\nAssistant: Git is a distributed version control system used for tracking code changes."},

    {"text": "User: Create exam notes on GitHub\nAssistant: GitHub is a platform for hosting and collaborating on Git repositories."},

    {"text": "User: Create exam notes on APIs\nAssistant: APIs allow different software applications to communicate with each other."},

    {"text": "User: Create exam notes on FastAPI\nAssistant: FastAPI is a Python framework used for building APIs quickly and efficiently."},

    {"text": "User: Create exam notes on Streamlit\nAssistant: Streamlit is a Python framework used to build interactive web apps easily."},

    {"text": "User: Create exam notes on transformers\nAssistant: Transformers are deep learning architectures designed for sequence modeling."},

    {"text": "User: Create exam notes on NLP\nAssistant: NLP enables computers to understand and process human language."},

    {"text": "User: Create exam notes on computer vision\nAssistant: Computer vision enables machines to interpret visual information from images and videos."},

    {"text": "User: Create exam notes on reinforcement learning\nAssistant: Reinforcement learning trains agents through rewards and punishments."},

    {"text": "User: Create exam notes on supervised learning\nAssistant: Supervised learning trains models using labeled datasets."},

    {"text": "User: Create exam notes on unsupervised learning\nAssistant: Unsupervised learning finds patterns in unlabeled data."},

    {"text": "User: Create exam notes on regression\nAssistant: Regression predicts continuous numerical values from data."},

    {"text": "User: Create exam notes on classification\nAssistant: Classification predicts categorical labels from input data."},

    {"text": "User: Create exam notes on decision trees\nAssistant: Decision trees split data into branches for predictions and classification."},

    {"text": "User: Create exam notes on random forest\nAssistant: Random forest combines multiple decision trees for improved accuracy."},

    {"text": "User: Create exam notes on KNN\nAssistant: KNN predicts outputs using the nearest neighboring data points."},

    {"text": "User: Create exam notes on logistic regression\nAssistant: Logistic regression is used for binary classification problems."},

    {"text": "User: Create exam notes on linear regression\nAssistant: Linear regression models relationships between variables using straight lines."},

    {"text": "User: Create exam notes on tensors\nAssistant: Tensors are multidimensional arrays used in deep learning computations."},

    {"text": "User: Create exam notes on PyTorch\nAssistant: PyTorch is a deep learning framework used for AI research and development."},

    {"text": "User: Create exam notes on TensorFlow\nAssistant: TensorFlow is a machine learning framework developed by Google."},

    {"text": "User: Create exam notes on pandas\nAssistant: Pandas is a Python library used for data analysis and manipulation."},

    {"text": "User: Create exam notes on NumPy\nAssistant: NumPy is a Python library used for numerical and array computations."},

    {"text": "User: Create exam notes on matplotlib\nAssistant: Matplotlib is a Python library used for data visualization."},

    {"text": "User: Create exam notes on statistics\nAssistant: Statistics involves collecting, analyzing, and interpreting data."},

    {"text": "User: Create exam notes on probability\nAssistant: Probability measures the likelihood of events occurring."},

    {"text": "User: Create exam notes on vectors\nAssistant: Vectors are quantities with both magnitude and direction."},

    {"text": "User: Create exam notes on algebra\nAssistant: Algebra studies mathematical symbols and equations."},

    {"text": "User: Create exam notes on calculus\nAssistant: Calculus studies change, motion, and accumulation."},

    {"text": "User: Create exam notes on trigonometry\nAssistant: Trigonometry studies relationships between angles and sides of triangles."},

    {"text": "User: Create exam notes on economics\nAssistant: Economics studies production, consumption, and distribution of resources."},

    {"text": "User: Create exam notes on business\nAssistant: Business involves activities related to goods, services, and profit generation."},

    {"text": "User: Create exam notes on marketing\nAssistant: Marketing promotes products and services to customers."},

    {"text": "User: Create exam notes on finance\nAssistant: Finance manages money, investments, and financial planning."},

    {"text": "User: Create exam notes on entrepreneurship\nAssistant: Entrepreneurship involves creating and managing businesses."},

    {"text": "User: Create exam notes on startups\nAssistant: Startups are newly established companies focused on scalable growth."},

    {"text": "User: Create exam notes on communication skills\nAssistant: Communication skills involve effectively sharing information and ideas."},

    {"text": "User: Create exam notes on leadership\nAssistant: Leadership is the ability to guide and motivate people toward goals."},

    {"text": "User: Create exam notes on teamwork\nAssistant: Teamwork involves people collaborating to achieve common objectives."},

    {"text": "User: Create exam notes on productivity\nAssistant: Productivity measures efficiency in completing tasks and goals."},

    {"text": "User: Create exam notes on time management\nAssistant: Time management is the process of organizing and planning time effectively."},

    {"text": "User: Create exam notes on problem solving\nAssistant: Problem solving involves identifying solutions to challenges or obstacles."},

    {"text": "User: Create exam notes on critical thinking\nAssistant: Critical thinking involves analyzing facts logically to make decisions."},

    {"text": "User: Create exam notes on creativity\nAssistant: Creativity is the ability to generate original ideas and solutions."},

    {"text": "User: Create exam notes on innovation\nAssistant: Innovation introduces new ideas, methods, or technologies."},

    {"text": "User: Create exam notes on robotics\nAssistant: Robotics involves designing and building programmable machines."},

    {"text": "User: Create exam notes on automation\nAssistant: Automation uses technology to perform tasks with minimal human intervention."}
]
