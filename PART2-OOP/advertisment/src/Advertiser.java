
public class Advertiser extends BaseAdvertising{
    private String name;
    private static int totalClicks = 0;

    public Advertiser(int id, String name) {
        super(id);
        this.name = name;
    }

    public String getName() {
        System.out.println("Advertiser--getName: " + name);
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public static void help(){
        //TODO: return string
    }

    public void incClicks() {
        super.incClicks();
        totalClicks += 1;
    }

    public static int getTotalClicks() {
        System.out.println("Advertiser--getTotalClicks: " + totalClicks);
        return totalClicks;
    }
}
