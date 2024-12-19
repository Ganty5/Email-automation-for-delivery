**Objective:**
The goal of this project was to automate email notifications for customers when their shipment status changes to "Delivered." This ensures timely communication and enhances customer satisfaction.

**What I Did:**

Dataset Creation: A synthetic dataset was generated containing shipment details such as ShipmentID, Origin, Destination, Status, EstimatedDelivery, and CustomerEmail.
Email Automation Setup: Using AWS Simple Email Service (SES), we configured verified email identities to send notifications. Python's boto3 library was used to interact with AWS SES for programmatically sending emails.
Dynamic Scheduling: We implemented a scheduling mechanism to check the dataset every 6 hours for shipments marked as "Delivered" and send notifications only once per shipment.
Custom Messages: Each email was personalized with shipment details, ensuring a professional and customer-centric approach.
Achievements:

Successfully automated email notifications for delivered shipments.
Implemented a system that prevents duplicate emails for the same shipment.
Demonstrated the integration of cloud-based services (AWS SES) with Python for real-world automation tasks.
Why This Matters:
Automation streamlines internal operations, reduces manual effort, and improves the customer experience. This project serves as a scalable solution for handling dynamic shipment updates and ensuring customers are always informed.
