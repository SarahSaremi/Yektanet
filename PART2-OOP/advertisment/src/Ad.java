public class Ad extends BaseAdvertising{
    private String title;
    private String imgURL;
    private String link;
    private Advertiser advertiser;
    private static final String description = "--- Ad Class Description ---\nEach object of this class represents an advertisement. \nAn advertisement contains a title, image and a link to advertiser's source.\n";

    public Ad(int id, String title, String imgURL, String link, Advertiser advertiser) {
        super(id);
        this.title = title;
        this.imgURL = imgURL;
        this.link = link;
        this.advertiser = advertiser;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getImgURL() {
        return imgURL;
    }

    public void setImgURL(String imgURL) {
        this.imgURL = imgURL;
    }

    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }


    @Override
    public void incClicks() {
        super.incClicks();
        this.advertiser.incClicks();
    }

    @Override
    public void incViews() {
        super.incViews();
        this.advertiser.incViews();
    }

    public void setAdvertiser(Advertiser advertiser) {
        this.advertiser = advertiser;
    }

    // Not included in the instructions.
    public Advertiser getAdvertiser() {
        return advertiser;
    }

    public static String describeMe() {
        return description;
    }

}
