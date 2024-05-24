from typing import Any
import requests

class TradeData:
	def __init__(self, data):
		self.created_on = data.get("CreatedOn")
		self.entity_id = data.get("EntityId")
		self.updated_on = data.get("UpdatedOn")
		self.armament_category_id = data.get("armamentCategoryId")
		self.armament_category_name = data.get("armamentCategoryName")
		self.armament_description = data.get("armamentDescription")
		self.armament_designation = data.get("armamentDesignation")
		self.armament_designation2 = data.get("armamentDesignation2")
		self.armament_designation3 = data.get("armamentDesignation3")
		self.armament_id = data.get("armamentId")
		self.armament_producer_company = data.get("armamentProducerCompany")
		self.armament_production_country = data.get("armamentProductionCountry")
		self.armament_sipri_estimate = data.get("armamentSipriEstimate")
		self.buyer_country = data.get("buyerCountry")
		self.deliveries = [self.parse_delivery(delivery) for delivery in data.get("deliveries", [])]
		self.order_date = data.get("orderDate")
		self.seller_country = data.get("sellerCountry")
		self.units_ordered = data.get("unitsOrdered")
		self.status = data.get("status1")

	def parse_delivery(self, delivery):
		return {
			"created_on": delivery.get("CreatedOn"),
			"entity_id": delivery.get("EntityId"),
			"updated_on": delivery.get("UpdatedOn"),
			"units": delivery.get("units"),
			"year": delivery.get("year")
		}

class TradeDataDeliveries:
	def __init__(self,data: dict[str, Any]):
		pass

	def toString(self):
		pass

class sipri_caller:
	def __init__(self):
		self.base_url = "https://atbackend.sipri.org/api/p/trades/getById"

	def get_order_by_id(self, trade_id):
		url = f"{self.base_url}?tradeId={trade_id}"
		response = requests.get(url)
		if response.status_code == 200:
			return TradeData(response.json())  # Parse the JSON response into the TradeData object
		else:
			return {"error": f"HTTP Error: {response.status_code} - {response.reason}"}

# Example usage:
# caller = sipri_caller()
# try:
# 	trade_data = caller.get_order_by_id("214613")
# 	print(f"Armament Category Name: {trade_data.armament_category_name}")
# 	print(f"Number of Deliveries: {len(trade_data.deliveries)}")
# 	for delivery in trade_data.deliveries:
# 		print(f"Delivery Entity ID: {delivery['entity_id']} - Units: {delivery['units']} - Year: {delivery['year']}")
# except requests.exceptions.RequestException as e:
# 	print("HTTP Request failed: ", e)
