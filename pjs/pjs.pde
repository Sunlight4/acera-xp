
void setup() {
  size(400, 400);
}
void buildFromXML(String xml) {
    XMLElement data = XMLElement.parse(xml);
    XMLElement[] xmlpoints = data.getChildren();
    for(int p=0, end=xmlpoints.length; p<end; p++) {
    XMLElement xmlpoint = xmlpoints[p];
    if (xmlpoint.getName() == "student") {
    int xp = xmlpoint.getIntAttribute("xp");
    int multiplier = xmlpoint.getIntAttribute("multiplier");
    String name = xmlpoint.getStringAttribute("name")
    String email = xmlpoint.getStringAttribute("email")
    //TODO: do stuff with data
    }
    }
   
    redraw(); 
  }
void draw() {
  background(255, 0, 255);
  fill(255, 255, 0);
  rect(mouseX - 5, mouseY - 5, 10, 10);
}
