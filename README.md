```bash
flippers
flippers order_service=full
flippers order_service=vegan
flippers courier=slow
flippers courier=premium
flippers order_service=vegan courier=slow
flippers courier=premium courier.fee=1.23
flippers order_service=full order_service.num_orders=25 order_service.smash_probability=0.3  courier=premium courier.fee=1.23
```
