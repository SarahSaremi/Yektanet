public class BaseAdvertising {
    private int id;
    private int clicks;
    private int views;

    public BaseAdvertising() {
    }

    public BaseAdvertising(int id) {
        this.id = id;
    }

    public int getClicks() {
        System.out.println("Base--getClicks: " + clicks);
        return clicks;
    }

    public int getViews() {
        System.out.println("Base--getViews: " + views);
        return views;
    }

    public void incClicks() {
        this.clicks += 1;
    }

    public void incViews() {
        this.views += 1;
    }

    public void describeMe(){
        //TODO: Return String
    }
}
