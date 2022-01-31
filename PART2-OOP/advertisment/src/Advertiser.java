
public class Advertiser extends BaseAdvertising{
    private String name;
    private static int totalClicks = 0;
    private static final String help = "--- Advertiser Help ---\nid -> A unique integer number for each advertiser. \nname -> A string representing advertiser's name. \nclick -> Total number of clicks of each advertiser. \nviews -> Total number of views of each advertiser.\n";
    private static final String description = "--- Advertiser Class Description ---\nEach object of this class represents an advertiser. \nAn advertiser can own multiple ads in the system.\n";

    public Advertiser(int id, String name) {
        super(id);
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public static String help(){
        return help;
    }

    public static String describeMe() {
        return description;
    }

    public void incClicks() {
        super.incClicks();
        totalClicks += 1;
    }

    public static int getTotalClicks() {
        return totalClicks;
    }
}
