//
//  HelloWorldViewController.m
//  HelloWorld
//
//  Created by Ali Nahm on 5/31/13.
//  Copyright (c) 2013 Ali Nahm. All rights reserved.
//

#import "HelloWorldViewController.h"

@interface HelloWorldViewController ()

@end

@implementation HelloWorldViewController
@synthesize userName = _userName;

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)changeGreeting:(id)sender {
    
    self.userName = self.textfield.text;
    
    NSString *nameString = self.userName;
    if ([nameString length] == 0) {
        nameString = @"World";
    }
    
    UILabel *myLabel = [[UILabel alloc]initWithFrame:CGRectMake(10, 50, 200, 40)];
    [myLabel setBackgroundColor:[UIColor clearColor]];
    [myLabel setText:@"Hi Label"];
    [[self view] addSubview:myLabel];
}

- (BOOL)textFieldShouldReturn:(UITextField *)theTextField {
    if (theTextField == self.textfield) {
        CGRect frameRect = self.textfield.frame;
        // [theTextField resignFirstResponder];
        [self.view endEditing:YES];
        CGRect labelframeRect = self.textfield.frame;
        
        if (frameRect.origin.y == labelframeRect.origin.y) {
            UIAlertView *alert = [[UIAlertView alloc] initWithTitle:@"No network connection"
                                                            message:@"You must be connected to the internet to use this app."
                                                           delegate:nil
                                                  cancelButtonTitle:@"OK"
                                                  otherButtonTitles:nil];
            [alert show];
        }
    }
    return YES;
}

@end
