# WhatsApp RSVP Bot

A scalable, conversational RSVP management system built with professional software architecture patterns. This project demonstrates enterprise-level design principles including the State Pattern, service layer architecture, and dependency injection applied to real-world event management automation.

## 🎯 Project Overview

This system automates RSVP collection for events through WhatsApp messaging, managing guest interactions at scale while maintaining a personalized, conversational experience. The architecture showcases production-ready patterns and modern Python development practices.

## ✨ Key Features

- **Conversational Natural Language Interface**: Multilingual support (Hebrew) with natural dialogue flow
- **Automated Data Collection**: Systematically gathers attendance confirmation, guest count, and preference data
- **State-Driven Architecture**: Implements the State Pattern for robust conversation flow management
- **Persistent Data Storage**: Google Sheets integration with real-time synchronization
- **Personalized Messaging**: Dynamic content based on guest data and context
- **Scalable Design**: Clean separation of concerns supporting multi-tenant deployments
- **Enterprise Integration**: WhatsApp Business API via Twilio for professional messaging infrastructure

## 🏗️ Architecture

The system follows professional software engineering patterns:

### **State Pattern Implementation**
Four conversation states manage the RSVP flow:
- `AwaitingAttendanceState`: Collects yes/no attendance confirmation
- `AwaitingGuestCountState`: Gets number of attending guests
- `AwaitingDietaryPreferencesState`: Collects dietary restrictions/preferences
- `CompletedState`: Terminal state after successful RSVP

Each state implements the abstract `ConversationState` interface, enabling polymorphic behavior and clean state transitions.

### **Service Layer Architecture**
```
API Layer (FastAPI)
    ↓
Service Layer (WhatsAppService)
    ↓
Domain Layer (ConversationState + Guest models)
    ↓
Integration Layer (Twilio + Google Sheets)
```

### **Hybrid Data Storage**
- **In-Memory Storage**: Temporary conversation state (workflow management)
- **Google Sheets**: Persistent guest data (business records)

This pragmatic approach balances performance requirements with data persistence needs while maintaining simplicity.

### **Dependency Injection**
Constructor injection throughout the codebase enables:
- Testability (easy mocking of dependencies)
- Flexibility (swap implementations without changing consumers)
- Clear dependency visualization

## 🛠️ Technology Stack

**Core Framework:**
- **FastAPI**: Modern, high-performance Python web framework
- **Python 3.8+**: Type hints and async/await support

**Integrations:**
- **Twilio WhatsApp Business API**: Professional messaging infrastructure
- **Google Sheets API**: Data persistence and guest management

**Architecture Patterns:**
- State Pattern for conversation flow
- Service Layer for business logic
- Abstract Base Classes (ABC) for interfaces
- Dependency Injection for loose coupling

## 📋 Prerequisites

- Python 3.8 or higher
- Twilio account with WhatsApp Business API access
- Google Cloud Platform account with Sheets API enabled
- Service account credentials for Google Sheets

## 🚀 Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd whatsapp-rsvp-bot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the root directory:
```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886
GOOGLE_SHEETS_CREDENTIALS_PATH=path/to/credentials.json
SPREADSHEET_ID=your_spreadsheet_id
```

### 4. Set Up Google Sheets
Create a Google Sheet with the following structure:
- Column A: Guest identifiers (names/IDs)
- Column B: Contact information (phone numbers in E.164 format)
- Column C: Attendance status (updated by system)
- Column D: Guest count (updated by system)
- Column E: Preferences/notes (updated by system)

### 5. Configure Google Cloud Service Account
1. Create a service account in Google Cloud Console
2. Enable Google Sheets API
3. Download the credentials JSON file
4. Share your spreadsheet with the service account email

### 6. Run the Application
```bash
uvicorn main:app --reload
```

### 7. Configure Twilio Webhook
In your Twilio Console, set the webhook URL for incoming WhatsApp messages:
```
https://your-domain.com/webhook/whatsapp
```

## 💬 System Workflow

### Conversation Flow

1. **Guest initiates conversation** → System retrieves guest profile from data store
2. **Personalized greeting** → Contextual welcome message in guest's language
3. **Attendance confirmation** → Binary response collection (attending/not attending)
4. **Guest count collection** (conditional) → Numeric input validation and processing
5. **Preference collection** → Free-text input for dietary restrictions or special requirements
6. **Confirmation and persistence** → Data validation and storage to Google Sheets
7. **State reset** → System ready for next guest interaction

### State Transitions

```
Start → AwaitingAttendance
         ↓ (yes)              ↓ (no)
    AwaitingGuestCount    → Completed
         ↓
    AwaitingDietary
         ↓
      Completed
```

### Data Flow

```
WhatsApp Message → FastAPI Webhook → WhatsAppService
                                          ↓
                                  ConversationState (polymorphic)
                                          ↓
                                  Google Sheets API
```

## 📁 Project Structure

```
whatsapp-rsvp-bot/
├── main.py                    # FastAPI application entry point
├── models/
│   ├── guest.py              # Guest domain model
│   └── conversation_state.py # State pattern implementation
├── services/
│   ├── whatsapp_service.py   # Core business logic
│   ├── twilio_client.py      # Twilio API integration
│   └── sheets_service.py     # Google Sheets integration
├── config/
│   └── settings.py           # Configuration management
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🎓 Core Competencies Demonstrated

This project demonstrates proficiency in:

**Software Architecture:**
- State Pattern for complex workflow management
- Service Layer architecture for separation of concerns
- Dependency Injection for testable, maintainable code
- High cohesion and loose coupling principles

**API Integration:**
- RESTful API development with FastAPI
- Third-party API integration (Twilio, Google Sheets)
- Webhook handling and event-driven architecture

**Data Management:**
- Hybrid storage strategies (in-memory + persistent)
- Runtime vs. persistent data separation
- Pragmatic engineering trade-offs

**Python Best Practices:**
- Type hints for code clarity
- Abstract Base Classes for interface definition
- Async/await for I/O operations
- Clean, readable code organization

## 💰 Cost-Effective Architecture

This solution demonstrates efficient resource utilization and cloud-native design:

**Commercial Event Management Platforms:** $320-380 USD (~1000-1200₪) per month for similar functionality at scale.

**This Implementation:**
- WhatsApp API (Twilio): ~ֿ\$0.005 per message × 600 messages = $3 (~11₪)
- Google Sheets API: Free tier
- Cloud hosting: $5-10/month (~18-36₪) or free tier

**Total Cost:** ~$8-13 (~30-47₪)

**Cost Reduction: 97%+** while maintaining enterprise-level architecture patterns and scalability.

This demonstrates the ability to make pragmatic engineering decisions that balance technical excellence with business value.

## 📄 License

This project is open source and available under the MIT License.

---

**Technical Focus**: This project demonstrates the application of enterprise-level software architecture patterns to event management automation, showcasing clean code principles, design patterns, and modern Python development practices.