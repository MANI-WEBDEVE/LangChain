from pydantic import BaseModel, Field , EmailStr

class User(BaseModel):
    name:str # Required the Field
    age:int|float # Required the Filed 
    is_emp:bool = True # Optional Beacse already default value 

# create a Object

user_data={'name':'MuhammadInam','age':12.2}

user=User(**user_data)
user_1=User.model_validate(user_data)

print(user)
print(user_1)


#  Data Types aur Validation (Field ka Use)
# Field-specific constraints lagana (min, max, regex, etc.)


class Employee(BaseModel):
    name: str = Field(...,description="provide a name", min_length=2, max_length=50)  # ... = Required
    email: str = Field(...,description="provide a email address", pattern=r"^[a-zA-Z0-9.+_-]+@gmail\.com$")  # @gmail.com hi chalega ya phie pydantic built in use karlo
    full_email:str=Field(EmailStr)
    salary: float = Field(gt=0, le=1000000)  # 0 < salary <= 10,00,000

emp = Employee.model_validate({
    "name": "Priya",
    "email": "priya@gmail.com",
    'full_email':'name@yahoo.com',
    "salary": 50000
})  # Works
print(emp)
# Invalid email (error aayega)
# invalid_emp = Employee.model_validate({"email": "priya@gmail.com",'full_email':'name@yahoo.com'}) 


# Nested Models (Real API Responses ke Liye)
# Complex data structures (jaise API responses) handle karna:

class Address(BaseModel):
    city: str
    pincode: str

class UserProfile(BaseModel):
    name: str
    address: Address  # Nested model
    phone_numbers: list[str]  # List of strings

    class Config:
        extra = 'ignore'  # Extra fields allow nahi (forbid) ya allow (allow) kar sakte hain

# Example data
data = {
    "name": "John Doe",
    "address": {
        "city": "New York",
        "pincode": "10001"
    },
    "phone_numbers": ["1234567890", "0987654321"],
    "extra_field": "This will be ignored"  # Extra field
}

user_profie = UserProfile.model_validate(data)
print(user_profie.address.pincode)
user_profie.address.pincode = "20001"  # Update nested field
print(user_profie)

# Config Class (Extra Fields Control)
# Model ka behavior customize karo (jaise extra fields allow karna ya nahi):

class ConfigDemo(BaseModel):
    name: str

    class Config:
        extra = 'forbid'  # Extra fields allow nahi
        # extra = 'allow'  # Extra fields allow
        frozen = True  # Model ko immutable banao (edit nahi kar sakte)


# Basic Validation with @field_validator (v2)
# Custom validation logic for single field:

from pydantic import BaseModel, field_validator

class Payment(BaseModel):
    card_number: str

    @field_validator('card_number')
    def validate_card(cls, value):
        card=cls.card_number=value
        print(card)

        if len(value) != 16 or not value.isdigit():
            raise ValueError('Invalid card number')
        return value


Payment.model_validate({"card_number": "1234567890123456"})  # Error: Invalid card