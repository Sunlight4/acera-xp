int theo_xp;
int xp;
int multiplier;
String name;
String email;

void setup() {
  size(400, 400);
}
void draw() {
  background(255, 0, 255);
  fill(255, 255, 0);
  rect(50, 175, theo_xp, 50);
  XML data = loadXML("http://acera-xp.appspot.com/xml");
  XML[] xmlpoints = data.getChildren();
  for(int p=0, end=xmlpoints.length; p<end; p++) {
  XML xmlpoint = xmlpoints[p];
  if (xmlpoint.getName() == "student") {
  int xp = xmlpoint.getInt("xp");
  int multiplier = xmlpoint.getInt("multiplier");
  String name = xmlpoint.getString("name");
  String email = xmlpoint.getString("email");
  println(name);
  if (name == "Theo") {
    theo_xp=xp;
    println(theo_xp);
  }
  //TODO: do stuff with data
  }
  }
  
}

