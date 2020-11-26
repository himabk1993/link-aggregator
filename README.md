# Betao Senior Back-End assignment

## Case

Netao is a tech startup that got traction selling a web application for a one-time fee of 100€. The process is simple: the user would go on their website, buy the service using a credit card, and Netao would then deliver access to the web application. Payments are currently collected through a third-party credit card processor. 

A business developer at Netao wants to increase revenue by switching to a subscription-based model. He suggests that by offering a SaaS (software-as-a-service) solution to their clients and lowering the initial fee, Netao will be able to collect recurring revenue and increase their turnover.

The project was approved, and now the engineering team is in charge of creating a subscription engine that is able to collect fees from users every month, as well as lock out users from accessing the web application if their payment fails or the subscription is cancelled.

Currently, Netao sells the web application for a one-time fee of 100€. The business analyst suggests selling the web application for 50€ and collecting a monthly recurring fee of 20€ for continuous access. The first month of access would be included in the initial 50€ fee.


Below are the current partial implementations of the User, Product and Purchase models. Currently, there is only one product, so has_access (whether or not the user can use the software) has been left on the User model.

```
/** PSEUDOCODE **/

class User
    /* Unique identifier */
    public int id
    /* Allows permanent access to the web application if the user has made a purchase */
    public boolean has_access

class Product
    /* Unique identifier */
    public int id
    public string name
    /* Recommended price */ 
    public float price

class Purchase:
    /* Buyer's ID */
    public int user_id // buyer
    /* product bought */
    public int product_id
    /* date of purchase */
    public date date
    /* actual price paid */
    public float price
``` 

You have been assigned the task to enhance Netao's system to be able to handle initial purchases, recurring subscriptions, payments, and product access. Here are the requirements we have gathered:

- Each Product (=software) has a recommended initial price and a recurring price. There is great likelihood that we will need to implement discounts for specific users later on.
- The initial price will be charged immediately as the user subscribes. The user will have access to the service for 30 days after the initial payment.
- The system needs to persist every payment made, by who, when and for what product.
- The recurring price will be charged every 30 days, and will kick in after 30 days from the initial subscription. For example, if a user buys the service on `2021-01-01T00:00` and pays the initial price, the system will attempt to charge her the recurring price at `2021-01-31T00:00`, then on `2021-03-02T00:00`, and so forth.
- If a recurring payment fails, the user will lose access to the service, and no further attempts at collecting payments will be made.
- A subscription can be cancelled at any time by the user. In that case she will retain access to the system until the end of the period, then lose access.
- In order to charge a user, the third-party payment processor only needs our internal user's ID and an amount. Currently, the system charges the user like so: `payment_processor.create_charge(user_id, amount)` and returns a transaction ID or fails.

## Tasks
- Suggest a data model to support those requirements. The model can be expressed in any language of your choice, including pseudocode such as above. The new data model needs to be able to express and persist transactions (payments made), subscriptions and product accesses (does the user have access to this product?).
- Suggest an algorithm to run recurring payments and manage software accesses using your suggested model.
- Suggest a way to run the payment engine in production so that users are charged continuously in a resilient manner.
