# Smart Office Assistant 

An intelligent AI-powered workplace management system that provides instant employee support through natural language processing. Pre-loaded with comprehensive company knowledge base - no uploads needed!

![Smart Office Assistant](https://img.shields.io/badge/Status-Ready%20to%20Use-brightgreen)
![Python](https://img.shields.io/badge/Python-3.7+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

##  Features

-  **AI-Powered Chat Interface** - Natural language processing for workplace queries
-  **Employee Management** - Pre-loaded employee database with profiles and information
-  **Leave Management** - Check balances, submit requests, and track time off
-  **Policy Information** - Instant access to company policies and procedures
-  **Benefits Information** - Complete benefits package details
-  **Remote Work Support** - Work from home policies and guidelines
-  **Real-time Dashboard** - Employee profile and leave balance sidebar
-  **Ready to Use** - No setup required, works immediately

##  Quick Start

### Prerequisites
- Python 3.7 or higher
- Modern web browser

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yashrajsingh1/smart-office-assistant.git
   cd smart-office-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the application**
   
   **Option 1: Use the startup script (Recommended)**
   ```bash
   START_SMART_OFFICE.bat
   ```
   
   **Option 2: Run directly**
   ```bash
   python smart_office_assistant.py
   ```

4. **Access the interface**
   - **Web Interface**: `smart_office_frontend.html` (opens automatically)
   - **API Documentation**: http://localhost:8002/docs
   - **Health Check**: http://localhost:8002/api/v1/health

## 💬 Usage Examples

### Chat Queries
The AI assistant understands natural language. Try asking:

- **Leave Management**:
  - "What is my leave balance?"
  - "I need sick leave tomorrow"
  - "I want to take vacation next week"

- **Employee Information**:
  - "Show my profile"
  - "Who is my manager?"
  - "What's my department?"

- **Company Policies**:
  - "What's the remote work policy?"
  - "What benefits do we have?"
  - "What's the leave policy?"

- **General Queries**:
  - "Contact information for HR"
  - "Company phone number"

### API Usage
```python
import requests

# Send a chat message
response = requests.post('http://localhost:8002/api/v1/chat', json={
    'message': 'What is my leave balance?',
    'employee_id': 'EMP001'
})

print(response.json())

# Get employee information
employee = requests.get('http://localhost:8002/api/v1/employees/EMP001')
print(employee.json())
```

##  Project Structure

```
smart-office-assistant/
├── smart_office_assistant.py    # Main FastAPI application
├── smart_office_frontend.html   # Web interface with sidebar
├── START_SMART_OFFICE.bat      # Windows startup script
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
├── .gitignore                # Git ignore rules
└── README.md                 # This documentation
```

## 🔧 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Root endpoint with system information |
| `/api/v1/health` | GET | Health check and system status |
| `/api/v1/chat` | POST | Main chat interface for AI queries |
| `/api/v1/employees/{id}` | GET | Get specific employee information |
| `/api/v1/employees` | GET | List all employees and departments |

##  Key Components

### Pre-loaded Employee Database
- **EMP001**: John Doe (Engineering, Senior Developer)
- **EMP002**: Sarah Wilson (Marketing, Marketing Manager)  
- **EMP003**: Mike Johnson (Sales, Sales Director)

### Company Knowledge Base
- **Leave Policies**: Annual, sick, personal, maternity, paternity leave
- **Remote Work**: Eligibility, options, requirements, core hours
- **Benefits**: Health insurance, 401k, fitness, learning budget
- **Contact Information**: HR, IT support, emergency contacts

### Smart Response System
- Context-aware responses based on employee profile
- Natural language understanding
- Intelligent query routing
- Personalized information delivery

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python) - High-performance async API
- **Frontend**: HTML5, Tailwind CSS, Vanilla JavaScript
- **AI Processing**: Custom natural language processing
- **Documentation**: OpenAPI/Swagger auto-generated
- **Server**: Uvicorn ASGI server

##  Development

### Running in Development Mode
```bash
python smart_office_assistant.py
```
The server automatically reloads when you make code changes.

### Adding New Features

1. **New Query Types**: Extend the `generate_smart_response()` function
2. **New Employees**: Add entries to the `employees_db` dictionary
3. **New Policies**: Update the `company_knowledge` structure
4. **UI Changes**: Modify `smart_office_frontend.html`

### Customization
- **Port**: Change port in the `uvicorn.run()` call
- **Employee Data**: Update `employees_db` with your organization's data
- **Company Policies**: Modify `company_knowledge` with your policies
- **Styling**: Customize CSS classes in the frontend

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes with proper documentation
4. Test thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Author

**Yashraj Singh**
- GitHub: [@yashrajsingh1](https://github.com/yashrajsingh1)
- LinkedIn: [Yashraj Singh](https://linkedin.com/in/yashrajsingh1)

##  Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/) for high-performance API development
- Styled with [Tailwind CSS](https://tailwindcss.com/) for modern, responsive design
- Icons from [Font Awesome](https://fontawesome.com/)
- Inspired by modern workplace automation and employee experience needs

##  Future Enhancements

- [ ] Integration with real HR systems
- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Mobile app companion
- [ ] Integration with calendar systems
- [ ] Automated leave approval workflows
- [ ] Slack/Teams bot integration

---

**Ready to revolutionize your workplace experience!** 

*This project demonstrates modern AI application development with clean, maintainable code and professional documentation.*
