from flask import Flask, render_template, request
from faker import Faker


app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    return render_template('creating_fake_user.html')

@app.route('/fake_profile', methods = ['GET'])
def fakeProfile():
    return render_template('create_fake_profile.html')

@app.route('/creating_fake_user_result', methods = ['GET','POST'])
def creatingFakeUserResult():
    if request.method == 'POST':
        fakeUserCount = request.form['fake_user_count']
        country = request.form['country']

        if fakeUserCount == '' or country == '':
            return 'Do not leave the fields blank'
        if fakeUserCount.isalpha():
            return 'Just enter integer.'
        if int(fakeUserCount) == 0 or int(fakeUserCount) < 0:
            return 'Error.'

        if int(fakeUserCount) == 1:
            try:
                fake = Faker(country)
                profileData = [[fake.first_name(),fake.last_name(),fake.user_name(),fake.password(),fake.month(),fake.text()] for i in range(1)]
                return render_template('creating_fake_user_result.html', fakeUser = profileData)
                
            except Exception as e:
                return 'Error : ' + str(e)
        else:
            fakeUser = []
            try:
                fake = Faker(country)
                profileData = [[fake.first_name(),fake.last_name(),fake.user_name(),fake.password(),fake.month(),fake.text()] for i in range(int(fakeUserCount))]
                return render_template('creating_fake_user_result.html', fakeUser = profileData)

            except Exception as e:
                return 'Error : ' + str(e)

    else:
        return 'For post requests only.'

@app.route('/creating_fake_profile_result', methods = ['GET','POST'])
def creatingFakeProfileResult():
    if request.method == 'POST':
        fakeProfile_ = []
        webSite = []

        fakeProfileCount = request.form['fake_profile_count']
        country = request.form['country']

        if fakeProfileCount == '' or country == '':
            return 'Do not leave the fields blank.'
        if fakeProfileCount.isalpha():
            return 'Just enter integer.'
        if int(fakeProfileCount) == 0 or int(fakeProfileCount) < 0:
            return 'Error.'

        try:
            fake = Faker(country)
            profileData = [fake.profile() for i in range(int(fakeProfileCount))]
            
            for profileData_ in profileData:
                if len(profileData_['website']) == 1:
                    webSite = ''.join(profileData_['website'])
                else:
                    webSite = profileData_['website']
                    webSite = ' '.join(webSite)

                fakeProfile_.append([
                    profileData_['job'],
                    profileData_['company'],
                    profileData_['ssn'],
                    profileData_['residence'],
                    profileData_['current_location'],
                    profileData_['blood_group'],
                    webSite,
                    profileData_['username'],
                    profileData_['name'],
                    profileData_['sex'],
                    profileData_['address'],
                    profileData_['mail'],
                    profileData_['birthdate']
                ])
                
            return render_template('create_fake_profile_result.html', 
            fakeProfile_= fakeProfile_, 
            profileKeys = list(profileData_.keys()))

        except Exception as e:
            return 'Error : ' + str(e)
    else:
        return 'For post requests only.'   

if __name__ == '__main__':
    app.run(debug=True, port=5000)
