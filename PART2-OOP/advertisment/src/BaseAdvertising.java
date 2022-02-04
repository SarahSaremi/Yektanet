public class BaseAdvertising {
    private int id;
    private int clicks;
    private int views;
    private static final String description = "--- BaseAdvertising Class Description ---\nAd and Advertiser inherit this class. \nThis class contains common fields and methods between these two classes.\n";

    public BaseAdvertising() {}

    public BaseAdvertising(int id) {
        this.id = id;
    }

    public int getClicks() {
        return clicks;
    }

    public int getViews() {
        return views;
    }

    public void incClicks() {
        this.clicks += 1;
    }

    public void incViews() {
        this.views += 1;
    }

    public static String describeMe(){
        return description;
    }
}
