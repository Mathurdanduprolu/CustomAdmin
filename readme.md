# Project setup script for Django Admin Customization Project

# Step 1: Clone the repository

echo "Cloning the repository..."
git clone https://github.com/yourusername/django-admin-customization.git
cd django-admin-customization || exit

# Step 2: Install the required Python packages

echo "Installing Python packages..."
pip install -r requirements.txt

# Step 3: Set up the database

echo "Setting up the database..."
python manage.py makemigrations
python manage.py migrate

# Step 4: Create media directories if they don't exist

echo "Setting up media directories..."
mkdir -p media

# Step 5: Configure media files in settings.py (This part needs to be done manually)

echo "Please make sure the following lines are added to your settings.py:"
echo "MEDIA_URL = '/media/'"
echo "MEDIA_ROOT = BASE_DIR / 'media'"

# Step 6: Start the Django development server

echo "Starting the Django development server..."
python manage.py runserver

echo "Setup complete! Visit http://127.0.0.1:8000/admin to see the customized admin interface."
