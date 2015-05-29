int theo_xp;
int xp;
int multiplier;
String name;
String email;

void setup() {
  size(400, 400);
}
void buildFromXML(String xml) {
  println("Build From XML... Check!");
  XMLElement data = new XMLElement(xml);
  XMLElement data = loadXML("http://acera-xp.appspot.com/xml");
  XMLElement[] xmlpoints = data.getChildren();
  for(int p=0, end=xmlpoints.length; p<end; p++) {
  XMLElement xmlpoint = xmlpoints[p];
  int xp = xmlpoint.getInt("xp");
  int multiplier = xmlpoint.getInt("multiplier");
  String name = xmlpoint.getString("name");
  String email = xmlpoint.getString("email");
  println(name);
  if (name.equals("Theo")) {
    println("We got Theo!");
    theo_xp=xp;
    println(theo_xp);
  }
  //TODO: do stuff with data
  }
  redraw();
}
void draw() {
  println("Draw... Check!");
  background(255, 0, 255);
  fill(255, 255, 0);
  rect(50, 175, theo_xp, 50);
}


