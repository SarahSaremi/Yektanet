public class Ad extends BaseAdvertising{
    private String title;
    private String imgURL;
    private String link;
    private Advertiser advertiser;

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

    public void incClicks() {
        super.incClicks();
        this.advertiser.incClicks();
    }

    public void incViews() {
        super.incViews();
        this.advertiser.incViews();
    }

    public void setAdvertiser(Advertiser advertiser) {
        this.advertiser = advertiser;
    }

}
