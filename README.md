# rPublisher
Team Name: Arnoldillo
Team members: Nathan Arnold, Dillon Tate

Individual contributions: TBD

Project design:
  Language: Python
  
  A graph database will be used to store precomputed distances from zip codes to treatment facilities.
  Given a patient zip code, map to the nearest hospitals with open beds. A node is created for each zip code containing at least one hospital.
  Node values: hospital_ids, zip_code
  Relationship properties: distance
  A query to this database would include the current zipcode and return the list of hopsital_ids in order of least to greatest distance.
  
  atlas: reallysecurepwd
  
  A complex event processor will be used to handle the event streams containing patient records.
  This CEP will be able to detect activity over time intervals to determine if there is an alert state. It will be used to handle the real time reporting APIs.
  
  A relational database will be used to keep track of hospital capacity and patient status.
  Entity: Patient
    Attributes: first_name, last_name, mrn, zip_code, patient_status_code, hospital_id
  Entity: Hospital
    Attributes: hospital_name, hospital_id, zip_code, max_capacity, current_capacity
  Relation: Patient <-> hospital
