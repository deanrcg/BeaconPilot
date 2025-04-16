// Admin panel JavaScript functionality

// Initialize tooltips
document.addEventListener('DOMContentLoaded', function() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
});

// Handle form submissions
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            // Add your form submission logic here
            console.log('Form submitted:', this);
        });
    });
});

// Handle user actions
document.addEventListener('DOMContentLoaded', function() {
    const userActions = document.querySelectorAll('.user-action');
    userActions.forEach(action => {
        action.addEventListener('click', function(e) {
            e.preventDefault();
            const actionType = this.dataset.action;
            const userId = this.dataset.userId;
            
            switch(actionType) {
                case 'edit':
                    // Handle edit action
                    console.log('Edit user:', userId);
                    break;
                case 'delete':
                    // Handle delete action
                    if (confirm('Are you sure you want to delete this user?')) {
                        console.log('Delete user:', userId);
                    }
                    break;
            }
        });
    });
});

// Handle modal actions
document.addEventListener('DOMContentLoaded', function() {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.addEventListener('show.bs.modal', function(e) {
            // Add any pre-modal show logic here
            console.log('Modal showing:', this);
        });
        
        modal.addEventListener('hidden.bs.modal', function(e) {
            // Add any post-modal hide logic here
            console.log('Modal hidden:', this);
        });
    });
});

// Handle alerts
function showAlert(message, type = 'success') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.role = 'alert';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    const container = document.querySelector('.container');
    container.insertBefore(alertDiv, container.firstChild);
    
    // Auto-dismiss after 5 seconds
    setTimeout(() => {
        const alert = bootstrap.Alert.getOrCreateInstance(alertDiv);
        alert.close();
    }, 5000);
} 