"""Canonical business, service and work taxonomy for transport and logistics."""
from copy import deepcopy
ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-TRANSPORT-LOGISTICS-SUPPLY-CHAIN-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
PARENT_ID = "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM"
STATUS = "CORE_CATALOG_ONLY"
TRANSPORT_BUSINESS_SERVICES = (
    {"id": "PASSENGER_TRANSPORT_BUSINESS", "name": "Passenger Transport Business", "description": "Commercial passenger transport operators and services."},
    {"id": "ROAD_TRANSPORT_BUSINESS", "name": "Road Transport Business", "description": "Commercial road passenger and goods transport."},
    {"id": "RAIL_TRANSPORT_BUSINESS", "name": "Rail Transport Business", "description": "Rail operators, freight and related services."},
    {"id": "AIR_TRANSPORT_BUSINESS", "name": "Air Transport Business", "description": "Airlines, airports, aviation and air cargo services."},
    {"id": "WATER_SHIPPING_BUSINESS", "name": "Water Transport and Shipping Business", "description": "Shipping, ferry, inland waterway and maritime services."},
    {"id": "FREIGHT_LOGISTICS_BUSINESS", "name": "Freight and Logistics Business", "description": "Freight forwarding, cargo handling and logistics providers."},
    {"id": "SUPPLY_CHAIN_BUSINESS", "name": "Supply Chain Business", "description": "Sourcing, planning, procurement and fulfilment coordination."},
    {"id": "COURIER_LAST_MILE_BUSINESS", "name": "Courier and Last-Mile Business", "description": "Parcel, courier, express delivery and last-mile distribution."},
    {"id": "WAREHOUSING_DISTRIBUTION_BUSINESS", "name": "Warehousing and Distribution Business", "description": "Warehousing, inventory handling and distribution."},
    {"id": "COLD_CHAIN_BUSINESS", "name": "Cold Chain Business", "description": "Temperature-controlled storage, transport and monitoring."},
    {"id": "FLEET_VEHICLE_SERVICES_BUSINESS", "name": "Fleet and Vehicle Services Business", "description": "Fleet ownership, leasing, maintenance and operations."},
    {"id": "MOBILITY_SERVICES_BUSINESS", "name": "Mobility Services Business", "description": "Ride-hailing, taxi, vehicle sharing and mobility platforms."},
    {"id": "BOOKING_TICKETING_BUSINESS", "name": "Transport Booking and Ticketing Business", "description": "Reservations, ticketing and passenger booking systems."},
    {"id": "PORT_TERMINAL_SERVICES_BUSINESS", "name": "Ports and Terminal Services Business", "description": "Port, terminal, cargo and intermodal handling."},
    {"id": "TRANSPORT_INFRASTRUCTURE_SERVICES_BUSINESS", "name": "Transport Infrastructure Services Business", "description": "Infrastructure operation, maintenance and specialist services."},
    {"id": "VEHICLE_RENTAL_LEASING_BUSINESS", "name": "Vehicle Rental and Leasing Business", "description": "Commercial vehicle hire, rental and leasing."},
    {"id": "TRANSPORT_MAINTENANCE_REPAIR_BUSINESS", "name": "Transport Maintenance and Repair Business", "description": "Vehicle, fleet, rail and transport asset maintenance."},
    {"id": "TRANSPORT_FINANCE_INSURANCE_BUSINESS", "name": "Transport Finance and Insurance Business", "description": "Transport asset finance, insurance and risk services."},
    {"id": "TRANSPORT_TECHNOLOGY_BUSINESS", "name": "Transport Technology Business", "description": "Fleet software, tracking, routing and transport technology."},
    {"id": "TRANSPORT_CONSULTING_COMPLIANCE_BUSINESS", "name": "Transport Consulting and Compliance Business", "description": "Planning, consulting, safety, licensing and regulatory services."},
)
def list_catalog():
    return deepcopy(list(TRANSPORT_BUSINESS_SERVICES))
