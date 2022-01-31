public class Main {
    public static void main(String args[]) {
        BaseAdvertising baseAdvertising = new BaseAdvertising();

        Advertiser advertiser1 = new Advertiser(1, "name1");
        Advertiser advertiser2 = new Advertiser(2, "name2");

        Ad ad1 = new Ad(1, "title1", "img-url1", "link1", advertiser1);
        Ad ad2 = new Ad(2, "title2", "img-url2", "link2", advertiser2);
        Ad ad3 = new Ad(3, "title3", "img-url3", "link3", advertiser2);

        baseAdvertising.describeMe();
        advertiser1.describeMe();

        ad1.incViews();
        ad1.incViews();
        ad1.incViews();
        ad1.incViews();
        ad1.incViews();
        ad2.incViews();

        ad1.incClicks();
        ad1.incClicks();

        ad2.incClicks();

        ad3.incClicks();
        ad3.incClicks();
        ad3.incClicks();

        advertiser2.getName();
        advertiser2.setName("new name");
        advertiser2.getName();

        ad1.getClicks();
        ad2.getClicks();
        ad3.getClicks();

        advertiser1.getClicks();
        advertiser2.getClicks();

        Advertiser.getTotalClicks();
        Advertiser.help();
    }
}
