using System;
using Aqua.VIC.Mobile.App.Models.Chat;
using Aqua.VIC.Mobile.App.Models.History;
using Syncfusion.DataSource;
using Xamarin.Forms.Internals;
using Xamarin.Forms.Xaml;
using Aqua.VIC.Mobile.App.DataService;

namespace Aqua.VIC.Mobile.App.Views.Chat
{
    /// <summary>
    /// Page to show chat message list
    /// </summary>
    [Preserve(AllMembers = true)]
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class ChatMessagePage
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="ChatMessagePage" /> class.
        /// </summary>
        public ChatMessagePage()
        {
            InitializeComponent();
            ///need to binding context from viewmodel
            BindingContext = ChatDataService.Instance.TheChatPageViewModel;
            ListView.DataSource.GroupDescriptors.Add(new GroupDescriptor
            {
                PropertyName = "Time",
                KeySelector = obj =>
                {
                    var item = obj as ChatMessage;
                 
                    return item.Time.Date;
                }
            });
        }

        private void SfButton_Clicked(object sender, EventArgs e)
        {
            //var app = Application.Current as App;
            //app.LoggedOut = true;

            //Navigation.PushModalAsync(new LoginPage());
            //DisplayAlert("Logging out", "Are you sure you want to log out?", "Yes", "Cancel");
            Navigation.PopAsync();
        }
    }
}