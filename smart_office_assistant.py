"""
Smart Office Assistant - AI-Powered Workplace Management System
A comprehensive office management solution with pre-loaded employee database
and company knowledge base for instant workplace assistance.

Author: Yashraj Singh
GitHub: https://github.com/yashrajsingh1
Created: 2025
"""

import time
import uuid
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Pydantic Models
class ChatMessage(BaseModel):
    message: str
    employee_id: str = "EMP001"

class ChatResponse(BaseModel):
    response: str
    employee_id: str
    timestamp: float
    sources: Optional[List[str]] = None

# Complete Employee Database - Pre-loaded for demonstration
employees_db = {
    "EMP001": {
        "id": "EMP001", 
        "name": "John Doe", 
        "email": "john.doe@techcorp.com",
        "department": "Engineering", 
        "position": "Senior Developer", 
        "manager": "Jane Smith",
        "leave_balance": {"annual": 18, "sick": 8, "personal": 4}, 
        "start_date": "2022-01-15",
        "salary": 95000, 
        "location": "New York", 
        "phone": "+1-555-0101"
    },
    "EMP002": {
        "id": "EMP002", 
        "name": "Sarah Wilson", 
        "email": "sarah.wilson@techcorp.com",
        "department": "Marketing", 
        "position": "Marketing Manager", 
        "manager": "Mike Johnson",
        "leave_balance": {"annual": 22, "sick": 10, "personal": 5}, 
        "start_date": "2021-03-10",
        "salary": 85000, 
        "location": "San Francisco", 
        "phone": "+1-555-0102"
    },
    "EMP003": {
        "id": "EMP003", 
        "name": "Mike Johnson", 
        "email": "mike.johnson@techcorp.com",
        "department": "Sales", 
        "position": "Sales Director", 
        "manager": "CEO",
        "leave_balance": {"annual": 25, "sick": 12, "personal": 6}, 
        "start_date": "2020-05-20",
        "salary": 110000, 
        "location": "Chicago", 
        "phone": "+1-555-0103"
    }
}

# Comprehensive Company Knowledge Base
company_knowledge = {
    "policies": {
        "leave_policy": """
🏖️ ANNUAL LEAVE: 0-2 years: 15 days, 3-5 years: 20 days, 6+ years: 25 days
🤒 SICK LEAVE: 10 days annually, medical certificate required for 3+ days
👨‍👩‍👧‍👦 PERSONAL LEAVE: 5 days annually, 48-hour notice required
🤱 MATERNITY LEAVE: 12 weeks paid
👨‍👶 PATERNITY LEAVE: 4 weeks paid
💔 BEREAVEMENT: 3 days immediate family, 1 day extended family
        """,
        "remote_work": """
🏠 REMOTE WORK POLICY:
✅ Eligibility: 6+ months tenure, satisfactory performance
📋 Options: 2 days remote, 3 days remote (senior), full remote (special cases)
🕐 Core Hours: 10 AM - 3 PM overlap required
📞 Communication: Daily standup, weekly team meeting
🔒 Security: VPN required, company laptop mandatory
        """,
        "benefits": """
💊 HEALTH INSURANCE: Full coverage for employee + family
🦷 DENTAL & VISION: Comprehensive coverage included
💰 401K MATCHING: Up to 6% company match
🏋️ FITNESS: Gym membership reimbursement $100/month
📚 LEARNING: $2000 annual professional development budget
🚗 PARKING: Free parking at all office locations
        """
    },
    "company_info": {
        "contact": "TechCorp Inc. | 123 Tech Street, Silicon Valley | +1-800-TECHCORP",
        "hr_email": "hr@techcorp.com",
        "it_support": "it-help@techcorp.com",
        "emergency": "security@techcorp.com"
    }
}

def generate_smart_response(message: str, employee_id: str) -> str:
    """Generate intelligent responses based on employee context and query"""
    
    message_lower = message.lower()
    employee = employees_db.get(employee_id, {})
    employee_name = employee.get('name', 'Employee')
    
    # Greeting responses
    if any(greeting in message_lower for greeting in ['hello', 'hi', 'hey', 'good morning', 'good afternoon']):
        return f"🌟 Welcome to Smart Office Assistant!\n\nHello {employee_name}! I'm pre-loaded with complete TechCorp knowledge - no uploads needed! I can help you with:\n\n🏖️ Leave Requests: \"I need sick leave tomorrow\"\n📋 Company Policies: \"What's the remote work policy?\"\n👤 Employee Info: \"Show my profile\"\n💼 Benefits: \"What benefits do we have?\"\n\nJust ask me anything in natural language!"
    
    # Leave balance queries
    if 'leave' in message_lower and any(word in message_lower for word in ['balance', 'remaining', 'left', 'how many']):
        if employee:
            leave_balance = employee.get('leave_balance', {})
            return f"📊 Your Current Leave Balance:\n\n🏖️ Annual Leave: {leave_balance.get('annual', 0)} days\n🤒 Sick Leave: {leave_balance.get('sick', 0)} days\n👨‍👩‍👧‍👦 Personal Leave: {leave_balance.get('personal', 0)} days\n\n💡 Need to request leave? Just tell me: \"I need sick leave tomorrow\" or \"I want to take vacation next week\""
        return "❌ I couldn't find your employee information. Please contact HR at hr@techcorp.com"
    
    # Leave requests
    if any(phrase in message_lower for phrase in ['sick leave', 'sick day', 'need sick', 'feeling sick']):
        return f"🤒 Sick Leave Request Noted!\n\nI understand you need sick leave tomorrow. Based on my knowledge:\n\n✅ You have {employee.get('leave_balance', {}).get('sick', 0)} sick days remaining\n📋 Action Items:\n• Notify your manager: {employee.get('manager', 'N/A')}\n• Submit medical certificate if >2 days\n• Update your calendar and out-of-office\n• Email team about coverage\n\n💊 Feel better soon! Let me know if you need anything else."
    
    if any(phrase in message_lower for phrase in ['vacation', 'annual leave', 'time off', 'holiday']):
        return f"🏖️ Vacation Request!\n\nI can help you with your vacation planning:\n\n✅ You have {employee.get('leave_balance', {}).get('annual', 0)} annual leave days\n📅 Remember to:\n• Submit request 2 weeks in advance\n• Coordinate with your team\n• Set up out-of-office messages\n• Brief your manager on pending tasks\n\n🌴 Where are you planning to go? Enjoy your time off!"
    
    # Policy queries
    if 'remote work' in message_lower or 'work from home' in message_lower or 'wfh' in message_lower:
        return f"🏠 Remote Work Policy:\n\n{company_knowledge['policies']['remote_work']}\n\n💡 Based on your profile, you're eligible for remote work options. Would you like me to help you plan your remote work schedule?"
    
    if 'benefits' in message_lower:
        return f"💼 TechCorp Benefits Package:\n\n{company_knowledge['policies']['benefits']}\n\n🎯 All benefits are active for you as a {employee.get('position', 'team member')}. Need specific benefit details? Just ask!"
    
    if 'leave policy' in message_lower or 'time off policy' in message_lower:
        return f"📋 Complete Leave Policy:\n\n{company_knowledge['policies']['leave_policy']}\n\n📊 Your current balance: Annual: {employee.get('leave_balance', {}).get('annual', 0)}, Sick: {employee.get('leave_balance', {}).get('sick', 0)}, Personal: {employee.get('leave_balance', {}).get('personal', 0)}"
    
    # Employee information
    if 'my profile' in message_lower or 'my info' in message_lower or 'show my' in message_lower:
        if employee:
            return f"👤 Your Employee Profile:\n\n🆔 ID: {employee['id']}\n👨‍💼 Name: {employee['name']}\n📧 Email: {employee['email']}\n🏢 Department: {employee['department']}\n💼 Position: {employee['position']}\n👔 Manager: {employee['manager']}\n📅 Start Date: {employee['start_date']}\n📍 Location: {employee['location']}\n📞 Phone: {employee['phone']}\n\n💡 Need to update any information? Contact HR at hr@techcorp.com"
        return "❌ Employee information not found. Please contact HR."
    
    # Manager queries
    if 'manager' in message_lower and any(word in message_lower for word in ['who', 'my', 'contact']):
        if employee:
            return f"👔 Your Manager: {employee.get('manager', 'Not specified')}\n\n💡 Need their contact info? I can help you find it, or check the company directory."
        return "❌ Manager information not available."
    
    # Company contact info
    if any(word in message_lower for word in ['contact', 'phone', 'address', 'office']):
        return f"📞 TechCorp Contact Information:\n\n{company_knowledge['company_info']['contact']}\n\n📧 Key Contacts:\n• HR: {company_knowledge['company_info']['hr_email']}\n• IT Support: {company_knowledge['company_info']['it_support']}\n• Emergency: {company_knowledge['company_info']['emergency']}"
    
    # Thank you responses
    if any(word in message_lower for word in ['thank', 'thanks', 'appreciate']):
        return f"😊 You're very welcome, {employee_name}!\n\nI'm here 24/7 to help with all your workplace needs. Feel free to ask me anything about:\n• Leave and time off\n• Company policies\n• Employee information\n• Benefits and perks\n\nHave a great day! 🌟"
    
    # Default intelligent response
    return f"🤔 I understand you're asking about: \"{message}\"\n\nBased on my knowledge base, I can help you with various topics. Could you be more specific? For example:\n\n🏖️ \"What's my leave balance?\"\n🏠 \"What's the remote work policy?\"\n👤 \"Show my profile\"\n💼 \"What benefits do we have?\"\n🤒 \"I need sick leave tomorrow\"\n\nJust ask me anything in natural language! 💬"

# Create FastAPI application
app = FastAPI(
    title="Smart Office Assistant",
    description="AI-powered workplace management system with pre-loaded employee database and company knowledge",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Smart Office Assistant API - Ready to Use!",
        "version": "1.0.0",
        "status": "operational",
        "employees_loaded": len(employees_db),
        "features": ["Employee Management", "Leave Tracking", "Policy Information", "AI Chat"]
    }

@app.get("/api/v1/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "version": "1.0.0",
        "database": "pre-loaded",
        "employees": len(employees_db),
        "knowledge_base": "ready"
    }

@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat_endpoint(message: ChatMessage):
    try:
        start_time = time.time()
        
        # Generate intelligent response
        response_text = generate_smart_response(message.message, message.employee_id)
        
        response_time = time.time() - start_time
        
        logger.info(f"Chat processed for {message.employee_id}: {message.message[:50]}...")
        
        return ChatResponse(
            response=response_text,
            employee_id=message.employee_id,
            timestamp=time.time()
        )
        
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/api/v1/employees/{employee_id}")
async def get_employee_info(employee_id: str):
    if employee_id not in employees_db:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employees_db[employee_id]

@app.get("/api/v1/employees")
async def list_employees():
    return {
        "employees": list(employees_db.keys()),
        "total": len(employees_db),
        "departments": list(set(emp["department"] for emp in employees_db.values()))
    }

if __name__ == "__main__":
    print("🚀 Smart Office Assistant AI - Ready to Use!")
    print("✅ Pre-loaded database - No uploads needed!")
    print("🌐 Open: smart_office_frontend.html")
    print("📖 API Docs: http://localhost:8002/docs")
    
    uvicorn.run("smart_office_assistant:app", host="0.0.0.0", port=8002, reload=True)
