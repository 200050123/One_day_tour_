from neo4j import GraphDatabase

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "your_password"  # Replace with your Neo4j password

driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

def close_driver():
    driver.close()

def store_user_preferences(preferences):
    with driver.session() as session:
        session.run("""
            MERGE (u:User {user_id: $user_id})
            SET u.city = $city, u.start_time = $start_time, u.end_time = $end_time,
                u.budget = $budget, u.interests = $interests
        """, **preferences)

def get_user_preferences(user_id):
    with driver.session() as session:
        result = session.run("MATCH (u:User {user_id: $user_id}) RETURN u", user_id=user_id)
        user_data = result.single()
        return user_data["u"] if user_data else None
