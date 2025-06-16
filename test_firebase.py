from firebase_init import db

def add_test_data():
    # This adds a document to 'test' collection
    db.collection('test').document().set({
        'message': 'Hello Firebase from Streamlit app'
    })

# CALL THE FUNCTION
add_test_data()

print("Test data added to Firebase!")
